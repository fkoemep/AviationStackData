import pendulum
from airflow import AirflowException
from airflow.decorators import task
from airflow.models import Connection


@task(retries=1, retry_delay=pendulum.duration(seconds=30))
def load(flight_data):
    from sqlalchemy import create_engine
    import pandas as pd

    testfligoo_connection = Connection.get_connection_from_secrets("testfligoo_connection")
    uri = testfligoo_connection.get_uri().replace('postgres://', 'postgresql://')
    engine = create_engine(uri)

    try:
        print('Loading the following flights to Postgres...')
        print(flight_data.to_json(orient='records', lines=True))
        with engine.begin() as conn:
            flight_data.to_sql('testfligoo', conn, if_exists="append", index=False)

    except Exception as e:
        raise AirflowException("Error while loading data to Postgres")





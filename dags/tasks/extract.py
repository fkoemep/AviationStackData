import pendulum
from airflow import AirflowException
from airflow.decorators import task
from airflow.models import Variable


@task(retries=3, retry_delay=pendulum.duration(seconds=30))
def extract():
    import requests
    import json
    import pandas as pd

    access_key = Variable.get("aviationstack_api_access_key", default_var=None)

    if access_key is not None:
        url = "http://api.aviationstack.com/v1/flights?limit=100&flight_status=active&access_key=" + access_key
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            data = r.json()['data']
            print('Extracted the following flights from AviationStack API:')
            print(json.dumps(data, indent=4, sort_keys=True))

            # unnest the data
            flight_data = pd.json_normalize(data=data)

            return flight_data

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
            raise AirflowException('Request failed. Maybe there is a problem with the API, your API key is invalid or '
                                   'you have exceeded the API request quota')

    raise AirflowException('No aviationstack_api_access_key found')

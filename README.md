## Flight Data ETL Process

A simple ETL process to extract flight data from Aviationstack flight API, transform the data, and load it into a postgres database.

Please keep in mind you should enter your own API key in the /secrets/variables.yaml file before using.

You can launch the ETL process from the Airflow web UI by triggering the aviationstack_process DAG and play with the data in a Jupyter Notebook that runs as an extra docker-compose service.

Airflow UI: http://localhost:8080

Juptyer Notebook: http://localhost:8888

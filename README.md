# Flight Data ETL Process

A simple ETL process that extracts flight data from Aviationstack flight API, transforms it, and loads it into a postgres database. A separate Jupyter Notebook running as an extra docker-compose service is also included to allow for data exploration.

This project uses the new Airflow 2.0 version that runs on docker-compose along with the new TaskFlow API. The LocalFilesystemBackend is used as a Secrets Engine to store the API key and the database credentials for security reasons.

The docker-compose file is based on the official Airflow docker-compose file with some modifications to include a Jupyter Notebook service.


## Usage
Please keep in mind you should enter your own API key in the /secrets/variables.yaml file before using.

To start the services, run the following command from the root directory:

```bash
docker-compose up
```

And you will be able to run the aviationstack_process DAG from the Airflow UI, after the process is finished you can explore the data using the Jupyter Notebook called data_consumer.

Airflow UI: http://localhost:8080

Juptyer Notebook: http://localhost:8888


You might also want to exclude the /secrets folder to avoid exposing your credentials to git, to do so run the following command:
```bash
git update-index --skip-worktree secrets/
```
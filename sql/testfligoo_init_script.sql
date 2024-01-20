-- CREATE DATABASE testfligoo;
-- GRANT ALL PRIVILEGES ON DATABASE testfligoo TO airflow;

CREATE TABLE IF NOT EXISTS testfligoo (
    flight_number INT NOT NULL,
    airline_name VARCHAR(60) NOT NULL,
    flight_date DATE NOT NULL,
    flight_status VARCHAR(20) NOT NULL,
    departure_airport VARCHAR(100) NOT NULL,
    departure_timezone VARCHAR(40) NOT NULL,
    arrival_airport VARCHAR(100) NOT NULL,
    arrival_timezone VARCHAR(40) NOT NULL,
    arrival_terminal CHAR(5),
    timestamp timestamptz NOT NULL DEFAULT NOW()
);
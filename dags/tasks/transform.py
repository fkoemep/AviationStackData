from airflow.decorators import task


@task()
def transform(flight_data):
    import pandas as pd
    from datetime import datetime

    # selecting the columns we're interested in
    flight_data = flight_data[['flight_date',
                               'flight_status',
                               'departure.airport',
                               'departure.timezone',
                               'arrival.airport',
                               'arrival.timezone',
                               'arrival.terminal',
                               'airline.name',
                               'flight.number',
                               ]]
    flight_data['departure.timezone'] = flight_data['departure.timezone'].str.replace('/', '-')
    flight_data['arrival.terminal'] = flight_data['arrival.terminal'].str.replace('/', '-')

    # renaming columns
    flight_data = flight_data.rename(columns={
        'flight_date': 'flight_date',
        'flight_status': 'flight_status',
        'departure.airport': 'departure_airport',
        'departure.timezone': 'departure_timezone',
        'arrival.airport': 'arrival_airport',
        'arrival.timezone': 'arrival_timezone',
        'arrival.terminal': 'arrival_terminal',
        'airline.name': 'airline_name',
        'flight.number': 'flight_number',
    })

    to_replace_nan = {
        'flight_date': datetime.now().strftime('%Y-%m-%d')
,
        'flight_status': 'active',
        'departure_airport': '-',
        'departure_timezone': '-',
        'arrival_airport': '-',
        'arrival_timezone': '-',
        'arrival_terminal': '-',
        'airline_name': '-',
        'flight_number': 0,
    }

    flight_data.fillna(value=to_replace_nan, inplace=True)

    return flight_data

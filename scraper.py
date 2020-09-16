from requests_html import HTMLSession
from datetime import datetime
from dateutil import tz
import re


def get_table(url, table_id):
    session = HTMLSession()
    r = session.get(url)

    table = r.html.find(f'#{table_id}', first=True)
    rows = table.find('tr')

    results = []

    timezone = tz.gettz('Europe/Bucharest')
    today = datetime.combine(datetime.now(tz=timezone), datetime.min.time())

    for row in rows:
        columns = row.find('td')

        if not columns:
            continue

        flight_number = columns[0]
        airline_name = None
        airline_logo_small = None
        airline_logo_big = None

        img = flight_number.find('img', first=True)
        if img:
            airline_name = img.attrs['title']
            airline_logo_small = img.attrs['src']
            airline_logo_big = airline_logo_small.replace('/small_', '/big_')
        flight_number = flight_number.text

        airport = columns[1].text
        airport_iata = None
        split_airport = re.findall(r'(.+) \(([A-Z]+)\)$', airport)
        if split_airport:
            airport, airport_iata = split_airport[0]

        scheduled_time = datetime.strptime(columns[2].text, '%H:%M').time()
        scheduled_timestamp = datetime.combine(today, scheduled_time, timezone)

        estimated_time = datetime.strptime(columns[3].text, '%H:%M').time()
        estimated_timestamp = datetime.combine(today, estimated_time, timezone)

        status = columns[4].text.upper()

        results.append({
            "flight_number": flight_number,
            "airline_name": airline_name,
            "airline_logo_small": airline_logo_small,
            "airline_logo_big": airline_logo_big,
            "airport": airport,
            "airport_iata": airport_iata,
            "scheduled_timestamp": scheduled_timestamp,
            "estimated_timestamp": estimated_timestamp,
            "status": status,
        })

    return results


def arrivals():
    url = 'https://www.bucharestairports.ro/en/flight-schedule/arrivals'
    table_id = 'sosiri'

    return get_table(url, table_id)


def departures():
    url = 'https://www.bucharestairports.ro/en/flight-schedule/departures'
    table_id = 'plecari'

    return get_table(url, table_id)


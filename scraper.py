from requests_html import HTMLSession
import re


def get_table(url, table_id):
    session = HTMLSession()
    r = session.get(url)

    table = r.html.find(f'#{table_id}', first=True)
    rows = table.find('tr')

    results = []

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

        scheduled_time = columns[2].text
        estimated_time = columns[3].text
        status = columns[4].text

        results.append({
            "flight_number": flight_number,
            "airline_name": airline_name,
            "airline_logo_small": airline_logo_small,
            "airline_logo_big": airline_logo_big,
            "airport": airport,
            "airport_iata": airport_iata,
            "scheduled_time": scheduled_time,
            "estimated_time": estimated_time,
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


import scraper


if __name__ == "__main__":
    arrivals = scraper.arrivals()
    departures = scraper.departures()

    print('ARRIVALS:')
    for entry in arrivals:
        print(
            f"{entry['flight_number']} - Scheduled {entry['scheduled_time']}, estimated {entry['estimated_time']}" +
            f" from {entry['airport_iata']} ({entry['airport']}) - {entry['status']}"
        )

    print('DEPARTURES:')
    for entry in departures:
        print(
            f"{entry['flight_number']} - Scheduled {entry['scheduled_time']}, estimated {entry['estimated_time']}" +
            f" from {entry['airport_iata']} ({entry['airport']}) - {entry['status']}"
        )
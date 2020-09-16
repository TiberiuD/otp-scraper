import scraper
from flask import Flask, jsonify
from flask_cors import CORS
import datetime
from dateutil import tz

app = Flask(__name__)
CORS(app)


def timestamp_is_current(timestamp):
    timezone = tz.gettz('Europe/Bucharest')
    beginning = datetime.datetime.now(tz=timezone) - datetime.timedelta(hours=1)
    end = datetime.datetime.now(tz=timezone) + datetime.timedelta(hours=3)

    if beginning <= timestamp <= end:
        return True

    return False


def convert_timestamps(data):
    for item in data:
        item['scheduled_timestamp'] = item['scheduled_timestamp'].isoformat()
        item['estimated_timestamp'] = item['estimated_timestamp'].isoformat()


@app.route('/departures')
def departures():
    all_departures = scraper.departures()
    convert_timestamps(all_departures)
    return jsonify(all_departures)


@app.route('/departures/current')
def current_departures():
    all_departures = scraper.departures()
    filtered_departures = []

    for item in all_departures:
        if timestamp_is_current(item['scheduled_timestamp']) or timestamp_is_current(item['estimated_timestamp']):
            filtered_departures.append(item)

    convert_timestamps(filtered_departures)
    return jsonify(filtered_departures)


@app.route('/arrivals')
def arrivals():
    all_arrivals = scraper.arrivals()
    convert_timestamps(all_arrivals)
    return jsonify(all_arrivals)


@app.route('/arrivals/current')
def current_arrivals():
    all_arrivals = scraper.arrivals()
    filtered_arrivals = []

    for item in all_arrivals:
        if timestamp_is_current(item['scheduled_timestamp']) or timestamp_is_current(item['estimated_timestamp']):
            filtered_arrivals.append(item)

    convert_timestamps(filtered_arrivals)
    return jsonify(filtered_arrivals)

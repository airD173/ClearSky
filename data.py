import requests
import json
import pandas as pd
import icon
import embeds


def main(zipcode):
    zipdb = pd.read_csv('zip_code_database.csv')
    latitude = zipdb[zipdb['zip'] == zipcode]['latitude'].values[0]
    longitude = zipdb[zipdb['zip'] == zipcode]['longitude'].values[0]
    coord = requests.get(f'https://api.weather.gov/points/{latitude},{longitude}').json()

    alerts = requests.get('https://api.weather.gov/alerts/active?zone=' + requests.get(coord['properties']['county']).json()['properties']['id']).json()


    forecast = requests.get(coord['properties']['forecast']).json()
    name = forecast['properties']['periods'][0]['name']
    temp = forecast['properties']['periods'][0]['temperature']
    thumb = icon.main(forecast['properties']['periods'][0]['icon'])
    short = forecast['properties']['periods'][0]['shortForecast']
    detailed = forecast['properties']['periods'][0]['detailedForecast']
    data1 = (zipcode, name, temp, thumb, short, detailed)
    name = forecast['properties']['periods'][1]['name']
    temp = forecast['properties']['periods'][1]['temperature']
    thumb = icon.main(forecast['properties']['periods'][1]['icon'])
    short = forecast['properties']['periods'][1]['shortForecast']
    detailed = forecast['properties']['periods'][1]['detailedForecast']
    data2 = (None, name, temp, thumb, short, detailed)
    return((data1, data2))

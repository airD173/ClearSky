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
    alertdata = requests.get('https://api.weather.gov/alerts/active?zone=' + requests.get(coord['properties']['county']).json()['properties']['id']).json()['features']
    forecast = requests.get(coord['properties']['forecast']).json()['properties']['periods']
    
    if len(alertdata) == 0:
        alerts = None
    else:
        alerts = alertdata
    
    data1 = (zipcode, forecast[0]['name'], forecast[0]['temperature'], icon.main(forecast[0]['icon']), forecast[0]['shortForecast'], forecast[0]['detailedForecast'])
    #data1 = (zipcode, name, temp, thumb, short, detailed)
    data2 = (alerts, forecast[1]['name'], forecast[1]['temperature'], icon.main(forecast[1]['icon']), forecast[1]['shortForecast'], forecast[1]['detailedForecast'])
    #data2 = (alerts, name, temp, thumb, short, detailed)
    
    return((data1, data2))


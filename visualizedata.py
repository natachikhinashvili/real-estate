import boto3
import pandas as pd
import folium
import requests
import matplotlib.pyplot as plt

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'selling-real-estate'

table = dynamodb.Table(table_name)

response = table.scan()
property_data = response['Items']

addresses = [item['address'] for item in property_data]

for address in addresses:
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={"AIzaSyBI5ZsMHPmb2o1SESN22PJi_Dqaba6CeYY"}'
    response = requests.get(url)
    data = response.json()
    print(data)
    
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
    else:
        print(f'Geocoding failed. Status: {data["status"]}')
    
    m = folium.Map(location=[latitude, longitude], zoom_start=12)
    
    folium.Marker(
        location=[latitude, longitude],
        popup=address
    ).add_to(m)

m.save("map.html")
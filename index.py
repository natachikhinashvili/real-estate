import requests
from bs4 import BeautifulSoup
import boto3

from realestate import get_data

def scrape_data():
    id = 1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url = "https://www.myhome.ge/en/s/?Keyword=Tbilisi&AdTypeID=1&mapC=41.73188365%2C44.8368762993663&cities=1996871&GID=1996871"
    collected_data = []
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            htmlelement = soup.find("html")
            if htmlelement:
                bodyelement = htmlelement.find("body")
                if bodyelement:
                    links = bodyelement.find_all("a", class_="card-container")
                    for link in links:
                        collected_data.append(get_data(link.get("href"), headers, id))
                        id+=1
        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)

    except Exception as e:
        print("An error occurred:", str(e))
    return collected_data

def insert_data(data):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = 'selling-real-estate'

    try:
        table = dynamodb.Table(table_name)


        response = table.get_item(Key={'id': data["id"]})

        if 'Item' not in response:
            response = table.put_item(
                Item={
                    "id": data["id"],
                    "name_last_name": data["name_last_name"],
                    "post_date": data["post_date"],
                    "price": data["price"],
                    "real_estate_type": data["real_estate_type"]
                }
            )
            print("New record inserted into DynamoDB.")
        else:
            print("Data already exists in DynamoDB. Not inserting.")

    except Exception as e:
        print("Error:", str(e))

def main():
    data = scrape_data()
    if data:
        for item in data:
            insert_data(item)

if __name__ == "__main__":
    main()

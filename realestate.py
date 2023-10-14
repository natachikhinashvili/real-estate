import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime
import boto3


def get_data(url, headers):    
    print(url, headers)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            htmlelement = soup.find("html")
            if htmlelement:
                bodyelement = htmlelement.find("body")
                if bodyelement:
                    detailpage = bodyelement.find("div", class_="detail-page")
                    name = detailpage.find("span", class_="name")
                    name = name.get_text()
                    date = detailpage.find("div", class_="date")
                    date = date.find("span").get_text()
                    price = detailpage.find("div", class_="price-box")
                    price = price.find("span").get_text().strip()
                    estatetype = detailpage.find("h1", class_="mb-0").get_text().lower().split(' ')
                    words_to_search = ["apartment", "house", "land", "hotel"]
                    match = ""
                    for word in words_to_search:
                        for estate in estatetype:
                            if word == estate:
                                match = estate

                    data = {
                        "name_last_name": name,
                        "post_date": date,
                        "price": price,
                        "real_estate_type": match
                    }
                    return data
    except Exception as e:
        print("An error occurred:", str(e))
    return None
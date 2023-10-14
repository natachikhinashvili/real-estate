import requests
from bs4 import BeautifulSoup
from datetime import datetime
import boto3

from realestate import get_data

def scrape_data():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url = "https://www.myhome.ge/en/s/?Keyword=Tbilisi&AdTypeID=1&mapC=41.73188365%2C44.8368762993663&cities=1996871&GID=1996871"
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
                        print(link.get("href"))
                        return get_data(link.get("href"), headers)
        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))
    return None


def main():
    data = scrape_data()
    print(data)
    if data:
        #insert_data_if_new(data)
        print(f"Data inserted into the cloud database at {datetime.now()}")

if __name__ == "__main__":
    main()

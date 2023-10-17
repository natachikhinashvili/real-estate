import requests
from bs4 import BeautifulSoup

def get_data(url, headers, id):
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
                    address = detailpage.find("span", class_="address").get_text().strip()
                    estatetype = detailpage.find("h1", class_="mb-0").get_text().lower().split(' ')
                    words_to_search = ["apartment", "house", "land", "hotel"]
                    match = ""
                    for word in words_to_search:
                        for estate in estatetype:
                            if word == estate:
                                match = estate

                    data = {
                        "id": id,
                        "name_last_name": name,
                        "post_date": date,
                        "price": price,
                        "real_estate_type": match,
                        "address": address
                    }
                    return data
    except Exception as e:
        print("An error occurred:", str(e))
    return None
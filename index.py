import json

from scrapedata import scrape_data
from insertdata import insert_data
from uploadtos3 import uploadtos3

def main():
    data = scrape_data()
    if data:
        with open("data.txt", "w") as file:
            data_str = [json.dumps(item) for item in data]
            data_str = "\n".join(data_str)
            file.write(data_str)
        uploadtos3()
        for item in data:
            insert_data(item)

if __name__ == "__main__":
    main()

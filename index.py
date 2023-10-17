from scrapedata import scrape_data
from insertdata import insert_data

def main():
    data = scrape_data()
    if data:
        for item in data:
            insert_data(item)

if __name__ == "__main__":
    main()

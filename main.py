from BeautifulSoup import scrape_stackoverflow
from bdd import connect_db, insert_data

if __name__ == "__main__":
    data = scrape_stackoverflow(pages=2)
    collection = connect_db()
    insert_data(collection, data)

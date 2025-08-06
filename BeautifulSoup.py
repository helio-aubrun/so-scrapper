import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

BASE_URL = "https://stackoverflow.com/questions"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_page(page=1):
    url = f"{BASE_URL}?tab=Newest&page={page}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Erreur HTTP {response.status_code} pour la page {page}")

def parse_question_block(block):
    title_elem = block.select_one("h3 a")
    summary_elem = block.select_one(".s-post-summary--content-excerpt")
    tag_elems = block.select(".s-post-summary--meta-tags .post-tag")
    author_elem = block.select_one(".s-user-card--link")
    time_elem = block.select_one("time")

    return {
        "title": title_elem.text.strip() if title_elem else None,
        "url": "https://stackoverflow.com" + title_elem["href"] if title_elem else None,
        "summary": summary_elem.text.strip() if summary_elem else None,
        "tags": [tag.text.strip() for tag in tag_elems],
        "author": author_elem.text.strip() if author_elem else None,
        "date": time_elem["datetime"] if time_elem and "datetime" in time_elem.attrs else None
    }

def scrape_stackoverflow(pages=1, delay=1):
    results = []
    for page in range(1, pages + 1):
        print(f"[INFO] Scraping page {page}...")
        html = fetch_page(page)
        soup = BeautifulSoup(html, "html.parser")
        questions = soup.select(".s-post-summary")
        for q in questions:
            data = parse_question_block(q)
            results.append(data)
        time.sleep(delay)
    return results

if __name__ == "__main__":
    data = scrape_stackoverflow(pages=2)
    for item in data:
        print(item)

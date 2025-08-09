import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://books.toscrape.com/"
START = urljoin(BASE, "catalogue/page-1.html")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; CohortScraper/1.0)"}

def get_soup(url: str) -> BeautifulSoup:
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def parse_book(card, category=None):
    title = card.h3.a["title"].strip()
    rel = card.h3.a["href"]
    product_url = urljoin(BASE, "catalogue/" + rel.replace("../../../", ""))
    price = card.select_one(".price_color").get_text(strip=True).replace("£", "")
    availability = card.select_one(".availability").get_text(strip=True)
    rating = next((c for c in card.select_one(".star-rating")["class"] if c != "star-rating"), "NA")
    return {
        "title": title,
        "price_gbp": price,
        "availability": availability,
        "rating_text": rating,
        "category": category or "",
        "product_url": product_url
    }

def page_heading(soup):
    h1 = soup.select_one(".page-header h1") or soup.select_one("h1")
    return h1.get_text(strip=True) if h1 else ""

def next_page(soup, current_url):
    link = soup.select_one("li.next a")
    return urljoin(current_url, link["href"]) if link else None

def scrape_all(start_url, out_csv="books.csv"):
    url = start_url
    seen = set()
    rows = []
    while url:
        soup = get_soup(url)
        category = page_heading(soup)
        for card in soup.select(".product_pod"):
            row = parse_book(card, category)
            key = (row["title"], row["product_url"])
            if key in seen:
                continue
            seen.add(key)
            rows.append(row)
        print(f"Scraped {len(rows)} items… ({url})")
        time.sleep(1)  # polite delay
        url = next_page(soup, url)

    cols = ["title","price_gbp","availability","rating_text","category","product_url"]
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"Done. Wrote {len(rows)} rows to {out_csv}")

if __name__ == "__main__":
    scrape_all(START, out_csv="books.csv")

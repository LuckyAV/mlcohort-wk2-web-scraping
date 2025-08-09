import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/page-1.html"
base = "https://books.toscrape.com/catalogue/"

books = []

while url:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        link = base + book.h3.a["href"].replace("../../", "")
        books.append([title, price, link])

    next_btn = soup.select_one(".next a")
    if next_btn:
        url = "https://books.toscrape.com/catalogue/" + next_btn["href"]
    else:
        url = None

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])
    writer.writerows(books)

print("Scraped", len(books), "books")
csv="books.csv")

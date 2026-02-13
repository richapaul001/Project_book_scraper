import time
import schedule
import os
from scraper.scrape import scrape_books
from scraper.csv_data import save_to_csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "books.csv")

def job():
    print("Running scheduler to extract price details...")
    books = scrape_books()
    save_to_csv(books,  DATA_PATH)
    print("Scraping completed successfully!")

# schedule.every(1).minutes.do(job)

job()

# while True:
#     schedule.run_pending()
#     time.sleep(1)


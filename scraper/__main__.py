from scrape import scrape_books
from csv_data import save_to_csv

if __name__ == "__main__":
    books = scrape_books()
    save_to_csv(books, "..\\data\\books.csv")
    print("Scraping completed successfully")
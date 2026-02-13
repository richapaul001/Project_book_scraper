import requests
from bs4 import BeautifulSoup
from scraper import config #importing URL from config file


def scrape_books(pages = 3):

    final_list = [] 

    for page in range(1, pages+1):

        url = config.BASE_URL.format(page)
        # print(url)
        response = requests.get(url)
        # print(response.status_code)

        #parsing through the response string
        soup = BeautifulSoup(response.text, "html.parser")

        books_list = soup.select(".product_pod")

        for book in books_list: 
            title_tag = book.h3.a["title"]
            price_tag = book.find(class_="price_color").text
            availability = book.select_one(".instock.availability").get_text(strip=True)
            rating = book.p["class"][1]
            
            if title_tag and price_tag and availability and rating: 
                final_list.append({"Title": title_tag,
                                "Price": price_tag,
                                "Availability": availability,
                                "Rating": rating
                                }) 
            
    return final_list


if __name__ == "__main__":
    data = scrape_books()
    print(f"Scraped {len(data)} books")
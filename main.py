import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
def get_html(url):

    response = requests.get(url)
    return response.text


def save_to_csv(data):
    keys = ['Title', 'Price', 'Rating']
    filename = 'books.csv'

    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(data)


def get_book_info():
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    for page in range(1, 6):
        url = base_url.format(page)
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        books = soup.find_all('article', class_='product_pod')
        for book in books:
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').text
            rating = book.find('p', class_='star-rating')['class'][1]

            print("Title:", title)
            print("Price:", price)
            print("Rating:", rating)
            print('------------------')

            data = {
                'Title': title,
                'Price': price,
                'Rating': rating
            }

            save_to_csv(data)


        sleep(randint(15, 20))



if __name__ == '__main__':
    get_book_info()




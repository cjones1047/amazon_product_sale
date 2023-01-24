import requests
from bs4 import BeautifulSoup


class AmazonScraping:

    def __init__(self, product_url):
        self.macbook_headers = {
            "Request Line": "GET / HTTP/1.1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,nl;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome"
                          "/109.0.0.0 Safari/537.36"
        }

        self.amazon_product_response = requests.get(
            url='https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91'
                'core/dp/B09JQK9DK5/ref=sr_1_2_sspa?'
                'crid=2SA42B2E0A0K7&keywords=mac%2Bbook&qid=1674511397&'
                'sprefix=mac%2Bbook%2Caps%2C109&sr=8-2-spons&'
                'spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4V0dZV1VQSDFONFcmZW5jcnlwdGVkSWQ9QTAwMjc'
                '3NDQzMlk1VVFVNTJBT1pJJmVuY3J5cHRlZEFkSWQ9QTA2MTQxNjcyRkVITENBNklGUzIyJnd'
                'pZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ'
                '1ZQ&th=1',
            headers=self.macbook_headers)
        self.amazon_product_response.raise_for_status()
        self.amazon_product_page = BeautifulSoup(self.amazon_product_response.text, "lxml")

    def get_product_title(self):
        product_title_element = self.amazon_product_page.find(id="productTitle",
                                                              class_="a-size-large product-title-word-break")
        product_title = product_title_element.text.strip()
        return product_title

    def get_product_price_float(self):
        product_price_str = self.amazon_product_page.find(class_="a-offscreen").text
        product_price_float = float(product_price_str[1:].replace(',', ''))
        return product_price_float

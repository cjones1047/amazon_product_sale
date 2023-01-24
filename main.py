from amazon_scraping import AmazonScraping

product_url = ('https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91'
               'core/dp/B09JQK9DK5/ref=sr_1_2_sspa?'
               'crid=2SA42B2E0A0K7&keywords=mac%2Bbook&qid=1674511397&'
               'sprefix=mac%2Bbook%2Caps%2C109&sr=8-2-spons&'
               'spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4V0dZV1VQSDFONFcmZW5jcnlwdGVkSWQ9QTAwMjc'
               '3NDQzMlk1VVFVNTJBT1pJJmVuY3J5cHRlZEFkSWQ9QTA2MTQxNjcyRkVITENBNklGUzIyJnd'
               'pZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ'
               '1ZQ&th=1')

amazon_scraping = AmazonScraping(product_url=product_url)
product_title = amazon_scraping.get_product_title()
product_price_float = amazon_scraping.get_product_price_float()

print(product_title)
print(product_price_float)

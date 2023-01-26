from amazon_scraping import AmazonScraping
from notification_manager import NotificationManager

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
current_price = amazon_scraping.get_product_price_float()

print(product_title)
print(current_price)

low_price_tracker_url = "https://camelcamelcamel.com/product/B09JQK9DK5"
lowest_price = amazon_scraping.get_lowest_historic_price(low_price_tracker_url=low_price_tracker_url)

print("Enter target price:")
target_price = f'${input("$")}'
notification_manager = NotificationManager()
recipient_email = input("Enter your email:\n")
if amazon_scraping.price_under_target(target_price=target_price, current_price=current_price):
    notification_manager.message_under_target(current_price=current_price,
                                              product_title=product_title,
                                              product_url=product_url,
                                              recipient_email=recipient_email)
else:
    notification_manager.message_over_target(current_price=current_price,
                                             product_title=product_title,
                                             product_url=product_url,
                                             lowest_price=lowest_price,
                                             recipient_email=recipient_email)

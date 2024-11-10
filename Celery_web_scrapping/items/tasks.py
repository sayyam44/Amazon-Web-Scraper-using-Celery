#this defines the tasks for the celery
from django.apps import apps #we cannot use .models import ProductScrapeEvent
from celery import shared_task
import helpers

@shared_task
def scrape_product_url_task(url):
    #open the url->scraping the url->save the scraped data

    if url is None:
        return 
    elif url == "":
        return
    
    #below we are getting the models that we need without importing the
    #actual class
    ProductScrapeEvent = apps.get_model('items', 'ProductScrapeEvent')
    
    # open the url
    html = helpers.scrape(url=url, solve_captcha=False)

    # scrape the url
    data = helpers.extract_amazon_product_data(html)

    # save the scraped data
    ProductScrapeEvent.objects.create_scrape_event(data, url=url)
    return 

@shared_task
def scrape_products_task(): 
    # this function batches the scraping process by iterating over 
    # active products(the products having active field as true) and 
    # passing their URLs to the scrape_product_url_task for further 
    # processing
    Product = apps.get_model('items', 'Product')
    qs = Product.objects.filter(active=True)
    for obj in qs:
        url = obj.url
        scrape_product_url_task.delay(url)
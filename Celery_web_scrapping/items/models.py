from django.db import models
from .tasks import scrape_product_url_task

# Represents an individual product, identified by its unique ASIN (Amazon Standard Identification Number). 
class Product(models.Model):
    asin = models.CharField(max_length=120, unique=True, db_index=True)
    url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=220, blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True, default=0.00)
    timestamp =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    metadata = models.JSONField(null=True, blank=True)
    active = models.BooleanField(default=True, help_text="Scrape daily?")
    trigger_scrape = models.BooleanField(default=False)
    _trigger_scrape = models.BooleanField(default=False)

    #we can scrape it whenever we save it and whenever we want
    # def save(self,*args,**kwargs):
    #     if self.url and self.pk:
    #         if self.trigger_scrape is not self._trigger_scrape:
    #             self.trigger_scrape=False
    #             self._trigger_scrape=False
    #             scrape_product_url_task.delay(self.url)
    #     super().save(*args,**kwargs)
         

# below - A custom manager for the ProductScrapeEvent model that 
# includes a method create_scrape_event.
class ProductScrapeEventManager(models.Manager):
    def create_scrape_event(self, data, url=None):
        asin = data.get('asin') or None
        if asin is None:
            return None
        product, _ = Product.objects.update_or_create(
            asin=asin,
            defaults={ #the fields that i want to update
                "url": url,
                "title": data.get('title') or "",
                "current_price": data.get('price') or 0.00,
                "metadata": data,
            }
        )
        event = self.create(
            product=product,
            url=url,
            asin=asin,
            data=data,
        )
        return event

# Below Represents individual scraping events for a product, storing 
# the scraped data and URL at the time of the event.
class ProductScrapeEvent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scrape_events')
    url = models.URLField(blank=True, null=True)
    data = models.JSONField(null=True, blank=True)
    asin = models.CharField(max_length=120, null=True, blank=True)
    
    objects = ProductScrapeEventManager()
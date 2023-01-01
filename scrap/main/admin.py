from django.contrib import admin
from .models import product_name , to_scrapper_data,price_data

# Register your models here.

admin.site.register(product_name)
admin.site.register(to_scrapper_data)
admin.site.register(price_data)

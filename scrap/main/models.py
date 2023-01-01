from django.db import models

from django.contrib.auth.models import User
from datetime import datetime

class product_name(models.Model):
    Name=models.CharField(max_length=300)
    

class to_scrapper_data(models.Model):
     url=models.CharField(max_length=3000)
     Name=models.CharField(max_length=3000)
     website_name=models.CharField(max_length=100)
     Name_Class_id=models.CharField(max_length=50)
     Price_Class_id=models.CharField(max_length=50)
     generated_by=models.ForeignKey(User,on_delete=models.CASCADE)
     generated_at=models.DateTimeField(default=datetime.now)

class price_data(models.Model):
    Product_name=models.CharField(max_length=3000)
    Price=models.IntegerField()
    website_name=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now)
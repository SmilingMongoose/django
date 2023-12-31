from django.db import models

# Create your models here.
class Visitor(models.Model):
    entered_visitor_name = models.CharField(max_length=200)

    def __str__(self):
        return self.entered_visitor_name
    
class Ticker(models.Model):
    ticker_name = models.CharField(max_length=200)

    def __str__(self):
        return self.ticker_name
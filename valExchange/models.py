from django.db import models
import requests

# Create your models here.
class Exchange():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        amount = float(amount)
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = amount * self.currencies[to_currency]
        return amount
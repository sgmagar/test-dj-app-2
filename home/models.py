from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Payment(models.Model):
    "Generated Model"
    paypal_email = models.EmailField(max_length=50,)
    paypal_id = models.CharField(max_length=200,)
    paypal_password = models.CharField(max_length=200,)
    paypal_currency = models.CharField(max_length=20,)
    paypal_receiver_email = models.EmailField(max_length=50,)

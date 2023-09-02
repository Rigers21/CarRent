from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.BigIntegerField()
    fuel = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='cars/images/', null=True)

    def __str__(self):
        return self.mark


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

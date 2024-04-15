from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    sum = models.PositiveIntegerField(default=0)

    product = models.ManyToManyField(Product, through='OrderAndProduct')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.status}'


class OrderAndProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product} - {self.count}'


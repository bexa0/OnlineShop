from django.contrib import admin
from app.models import *

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderAndProduct)

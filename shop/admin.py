from django.contrib import admin
from .models import Restaurant,Item,Menu,Order,orderItem
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(orderItem)
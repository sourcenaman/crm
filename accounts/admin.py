from django.contrib import admin
from .models import Customer, Product, Orders, Tag

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Tag)

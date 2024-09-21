from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    
    fields = [
        "name",
        "price",
        "category",
        "brand",
        "seller",
        "warranty",
        "product_type",
        "image"
    ]
    
    list_display = [
        "name",
        "price"
    ]
    
admin.site.register(Product, ProductAdmin)
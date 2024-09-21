from django.contrib import admin
from .models import Categories, Brand, Seller, Warranty, ProductType

class CategoriesAdmin(admin.ModelAdmin):
    
    fields = [
        "category_name",
        "category_vale",

    ]
    
    list_display = [
        "category_name",
    ]
    
admin.site.register(Categories, CategoriesAdmin)

class BrandAdmin(admin.ModelAdmin):
    
    fields = [
        "brand_name",
        "brands_vale",

    ]
    
    list_display = [
        "brand_name",
    ]
    
admin.site.register(Brand, BrandAdmin)

class SellerAdmin(admin.ModelAdmin):
    
    fields = [
        "seller_name",
        "seller_vale",

    ]
    
    list_display = [
        "seller_name",
    ]
    
admin.site.register(Seller, SellerAdmin)

class WarrantyAdmin(admin.ModelAdmin):
    
    fields = [
        "warranty_name",
        "warranty_vale",

    ]
    
    list_display = [
        "warranty_name",
    ]
    
admin.site.register(Warranty, WarrantyAdmin)

class ProductTypeAdmin(admin.ModelAdmin):
    
    fields = [
        "product_type_name",
        "product_type_vale",

    ]
    
    list_display = [
        "product_type_name",
    ]
    
admin.site.register(ProductType, ProductTypeAdmin)

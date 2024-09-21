from django.db import models


class Categories(models.Model):
    
    category_name = models.CharField(max_length=255)
    category_vale = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.category_name
    
    
class Brand(models.Model):
    
    brand_name = models.CharField(max_length=255)
    brands_vale = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.brand_name
    
    
class Seller(models.Model):
    
    seller_name = models.CharField(max_length=255)
    seller_vale = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.seller_name
    
    
class Warranty(models.Model):
    
    warranty_name = models.CharField(max_length=255)
    warranty_vale = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.warranty_name
    
    
class ProductType(models.Model):
    
    product_type_name = models.CharField(max_length=255)
    product_type_vale = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.product_type_name
from django.db import models
from Category.models import Categories, Brand, Seller, Warranty, ProductType


class Product(models.Model):
    
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name="products", null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products", null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, related_name="products", null=True, blank=True)
    warranty = models.ForeignKey(Warranty, on_delete=models.PROTECT, related_name="products", null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name="products", null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    @property
    def imageURL(self):
        
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.name
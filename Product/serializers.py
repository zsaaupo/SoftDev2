from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "category",
            "brand", "seller",
            "warranty",
            "product_type",
            "image"
        ]
from django.shortcuts import render
from .models import Product
from Category.models import Categories, Brand, Seller, Warranty, ProductType
from .serializers import ProductSerializer
from django.db.models import Q

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.utils import json

class ProductList(ListAPIView):
    
    permission_classes=[]
    
    def get(self, request):
        
        product_list = Product.objects.all().order_by("name")
        product_list = ProductSerializer(product_list, many=True).data
        
        return Response(product_list)
    
class FilterProduct(CreateAPIView):
    
    permission_classes = []
    
    def post(self, request):
        result = {}
        
        try:
            data = json.loads(request.body)
            
            categories = data.get("category", [])
            brands = data.get("brand", [])
            sellers = data.get("seller", [])
            warranties = data.get("warranty", [])
            product_types = data.get("productType", [])
            sortByprice = data.get("price", [])
            
            filtered_product = {}

            if categories:
                filtered_product['category__in'] = categories
            if brands:
                filtered_product['brand__in'] = brands
            if sellers:
                filtered_product['seller__in'] = sellers
            if warranties:
                filtered_product['warranty__in'] = warranties
            if product_types:
                filtered_product['product_type__in'] = product_types
            if not filtered_product:
                products = Product.objects.all()
            else:
                products = Product.objects.filter(**filtered_product)
                
            if sortByprice == [1]:
                products = products.order_by("-price")
            else:
                products = products.order_by("price")
  
            serializer = ProductSerializer(products, many=True).data
            
            return Response(serializer)
        except Exception as ex:
            result = {}
            result['message'] = str(ex)
            return Response(result)
        

class SearchApi(CreateAPIView):
    permission_classes = []

    def post(self, request):
        try:
            
            data = json.loads(request.body)
            searchValue = data['searchValue']
            products = Product.objects.all()

            if searchValue:
                products = products.filter(
                    Q(name__icontains=searchValue) |
                    Q(category__category_name__icontains=searchValue) |
                    Q(brand__brand_name__icontains=searchValue) |
                    Q(seller__seller_name__icontains=searchValue) |
                    Q(product_type__product_type_name__icontains=searchValue)
                )

            products = ProductSerializer(products, many=True).data
            return Response(products)
        
        except Exception as ex:
            result = {}
            result['message'] = str(ex)
            return Response(result)
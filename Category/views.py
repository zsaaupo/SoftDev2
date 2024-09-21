from django.shortcuts import render
from .models import Categories, Brand, Seller, Warranty, ProductType

def landingPage(request):

    allCategories = Categories.objects.all().order_by("category_name")
    allBrands = Brand.objects.all().order_by("brand_name")
    allSellers = Seller.objects.all().order_by("seller_name")
    allWarrantys = Warranty.objects.all().order_by("warranty_name")
    allProductTypes = ProductType.objects.all().order_by("product_type_name")
    return render(request, "landing.html", {
        "Categories": allCategories, 
        "Brands": allBrands,
        "Sellers": allSellers, 
        "Warrantys": allWarrantys, 
        "ProductTypes": allProductTypes
    })
from django.urls import path
from .views import ProductList, FilterProduct, SearchApi

urlpatterns = [
    path('', ProductList.as_view()),
    path('filter/', FilterProduct.as_view()),
    path('search/', SearchApi.as_view()),
]

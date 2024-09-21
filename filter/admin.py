from django.contrib import admin
from .models import Category, Option

class CategoryAdmin(admin.ModelAdmin):
    
    fields = [
        "category_name"
    ]
    
    list_display = [
        "category_name"
    ]

admin.site.register(Category, CategoryAdmin)

class OptionAdmin(admin.ModelAdmin):
    
    fields = [
        "categories",
        "option_name",
        "option_value"
    ]
    
    list_display = [
        "option_name",
        "categories"
    ]

admin.site.register(Option, OptionAdmin)
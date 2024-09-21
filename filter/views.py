from django.shortcuts import render
from .models import Category, Option


def landingPage(request):

    all_filter = Category.objects.prefetch_related("options").all().order_by("category_name")
    return render(request, "landing.html", {"allFilter": all_filter})
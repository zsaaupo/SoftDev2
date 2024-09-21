from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "full_name",
        "email",
        "phone_number"
    ]

    readonly_fields = [
        "slug",
        "otp"
    ]

admin.site.register(Customer, CustomerAdmin)
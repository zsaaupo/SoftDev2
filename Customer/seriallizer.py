from rest_framework import serializers
from .models import Customer

class CustomarSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = ["full_name", "email", "phone_number", "address", "slug"]

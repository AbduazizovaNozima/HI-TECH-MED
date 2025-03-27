from .models import *
from rest_framework import serializers


# class CategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Category
#         fields = (
#             'id', 'name', 'icon', 'order'
#         )

class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = (
            'full_name', 'position', 'image', 'description'
        )

        
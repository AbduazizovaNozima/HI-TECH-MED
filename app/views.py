from django.shortcuts import render
from .models import *
from rest_framework import views
from . import serializers
from rest_framework.response import Response

# class CategoryListAPIViews(views.APIView):

#     def get(self, request):
#         data = Category.objects.filter()
#         serializer = serializers.CategorySerializer(data, many=True)
#         return Response(
#             data=serializer.data,)
    

class CustomersListAPIViews(views.APIView):

    def get(self, request):
        data = Customers.objects.all()
        serializer = serializers.CustomersSerializer(data, many=True)
        return Response(
            data=serializer.data,)
    


from django.shortcuts import render
from rest_framework import generics
from .models import SalesModel
from .serializers import MyModelSerializer

class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = MyModelSerializer

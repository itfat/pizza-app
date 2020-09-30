from django.shortcuts import render
from rest_framework import viewsets
from .models import Pizza
from .serializers import PizzaOrderSerializer

# Create your views here.

class PizzaOrderView(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class =  PizzaOrderSerializer

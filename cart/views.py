from django.shortcuts import render
from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
# Create your views here.

class CartView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
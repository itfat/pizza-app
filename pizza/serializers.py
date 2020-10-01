from rest_framework import serializers
from .models import Pizza
from cart.models import Cart

class PizzaOrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    class Meta:
        model = Pizza
        fields = ('category', 'size', 'price', 'image')

   

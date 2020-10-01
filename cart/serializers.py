from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    # created_by = serializers.CurrentUserDefault()
    pizza = PizzaOrderSerializer()
    class Meta:
        model = Cart
        fields = ('category', 'size')
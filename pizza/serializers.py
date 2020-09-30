from rest_framework import serializers
from .models import Pizza

class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('pk', 'category', 'size', 'price', 'image')

   

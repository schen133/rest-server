from rest_framework import serializers
from base.models import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    

# this will be serializing the data user try to send to the API through a POST request


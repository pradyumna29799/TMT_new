from rest_framework import serializers

from products.models import Product


class ProducrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
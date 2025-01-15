from rest_framework import serializers
from suppliers.models import Supplier

class supplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
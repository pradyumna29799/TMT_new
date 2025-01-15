from rest_framework import serializers
from .models import Warehouse
from django.contrib.auth.models import User


class WarehouseSerializer(serializers.ModelSerializer):
    manager_name = serializers.SerializerMethodField()

    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'location', 'created_at', 'updated_at', 'manager', 'manager_name']

    def get_manager_name(self, obj):
        try:
            # Fetch the manager's user object and concatenate first_name and last_name
            return f"{obj.manager.first_name} {obj.manager.last_name}"
        except User.DoesNotExist:
            return None
from django.shortcuts import render

from warehouses.serializers import WarehouseSerializer
from .models import Warehouse
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class WarehouseListView(ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]   
class WarehouseDetailView(RetrieveAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]
class WarehouseCreateView(CreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]
class WarehouseUpdateView(UpdateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]
class WarehouseDeleteView(DestroyAPIView):
    queryset = Warehouse.objects.all()
    permission_classes = [IsAuthenticated]

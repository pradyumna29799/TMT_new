from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from suppliers.serializers import supplierSerializer
from .models import Supplier
# Create your views here.
class SupplierListView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = supplierSerializer
    permission_classes = [IsAuthenticated]   
class SupplierDetailView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = supplierSerializer
    permission_classes = [IsAuthenticated]
class SupplierCreateView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = supplierSerializer
    permission_classes = [IsAuthenticated]
class SupplierUpdateView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = supplierSerializer
    permission_classes = [IsAuthenticated]
class SupplierDeleteView(DestroyAPIView):
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]
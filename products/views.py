from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Product,Category
from .serializers import CategorySerializer, ProducrSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducrSerializer
    permission_classes = [IsAuthenticated]
    
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducrSerializer
    permission_classes = [IsAuthenticated]

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducrSerializer
    permission_classes = [IsAuthenticated]

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducrSerializer
    permission_classes = [IsAuthenticated]

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

class CategoryViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
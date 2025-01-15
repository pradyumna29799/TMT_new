from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Product,Category, Unit
from .serializers import CategorySerializer, ProducrSerializer, UnitSerializer
from rest_framework.permissions import IsAuthenticated

############################################## Product CRUD APIS #########################################################################
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

############################################## Category CRUD APIS #########################################################################

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]   
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    
############################################## unit CRUD APIS #########################################################################

class UnitListView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]   
class UnitDetailView(RetrieveAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]
class UnitCreateView(CreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]
class UnitUpdateView(UpdateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]
class UnitDeleteView(DestroyAPIView):
    queryset = Unit.objects.all()
    permission_classes = [IsAuthenticated]
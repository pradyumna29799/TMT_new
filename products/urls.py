from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    
    path('', views.ProductListView.as_view(), name='Product-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='Product-detail'),
    path('create/', views.ProductCreateView.as_view(), name='Product-create'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='Product-update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='Product-delete'),
    
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    
    path('unit/', views.UnitListView.as_view(), name='unit-list'),
    path('unit/<int:pk>/', views.UnitDetailView.as_view(), name='unit-detail'),
    path('unit/create/', views.UnitCreateView.as_view(), name='unit-create'),
    path('unit/<int:pk>/update/', views.UnitUpdateView.as_view(), name='unit-update'),
    path('unit/<int:pk>/delete/', views.UnitDeleteView.as_view(), name='unit-delete'),


    
    
]


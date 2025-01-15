from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members'),
    path('', views.WarehouseListView.as_view(), name='warehouse-list'),
    path('<int:pk>/', views.WarehouseDetailView.as_view(), name='warehouse-detail'),
    path('create/', views.WarehouseCreateView.as_view(), name='warehouse-create'),
    path('<int:pk>/update/', views.WarehouseUpdateView.as_view(), name='warehouse-update'),
    path('<int:pk>/delete/', views.WarehouseDeleteView.as_view(), name='warehouse-delete'),


]
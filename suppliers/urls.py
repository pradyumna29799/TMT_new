from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members'),
    
    path('', views.SupplierListView.as_view(), name='supplier-list'),
    path('<int:pk>/', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('create/', views.SupplierCreateView.as_view(), name='supplier-create'),
    path('<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier-delete'),

]
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    # path('members/', views.members, name='members'),
    path('', views.ProductListView.as_view(), name='Product-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='Product-detail'),
    
    path('create/', views.ProductCreateView.as_view(), name='Product-create'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='Product-update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='Product-delete'),
]
router.register(r'category', views.CategoryViewSet, basename='Category')
urlpatterns = router.urls

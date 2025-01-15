from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members'),
    path('create-user/', views.UserCreateView.as_view(), name='create_user'),
    path('roles/', views.RoleListView.as_view(), name='roles_user'),
    path('roles/create', views.RoleCreateView.as_view(), name='roles_user'),
    
    path('user-list/', views.UerListView.as_view(), name='user_list'),
    path('user-list/<int:pk>/', views.UerDetailView.as_view(), name='user_list-detail'),
    path('user-list/<int:pk>/update/', views.UerUpdateView.as_view(), name='user_list-update'),
    path('user-list/<int:pk>/delete/', views.UerDeleteView.as_view(), name='user_list-delete'),
    
    path('warehouse-manager/', views.WarehouseManagerUsersView.as_view(), name='warehouse_manager'),


    
]
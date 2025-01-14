from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members'),
    path('create-user/', views.UserCreateView.as_view(), name='create_user'),
]
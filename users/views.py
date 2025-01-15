from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from users.models import Role, UserProfile
from users.serializers import CustomTokenObtainPairSerializer, RoleSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .serializers import UserProfileSerializer

# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]      
class RoleCreateView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
    
    
class UerListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  
class UerDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
class UerUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
class UerDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class WarehouseManagerUsersView(APIView):
    def get(self, request):
        # Filter UserProfiles by role name 'Warehouse Manager'
        user_profiles = UserProfile.objects.filter(role__name='Warehouse Manager').select_related('role', 'user')

        if not user_profiles.exists():
            return Response({"detail": "No users found with the role 'Warehouse Manager'"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the user profiles
        serializer = UserProfileSerializer(user_profiles, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
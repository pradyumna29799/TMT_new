from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Call the parent method to get the token data
        data = super().validate(attrs)

        # Get the user object
        user = self.user

        # Check if the user has a related profile and if the profile has a role
        try:
            role_id = user.userprofile.role.id if user.userprofile and user.userprofile.role else None
        except UserProfile.DoesNotExist:
            role_id = None

        # Check if the role_id is 1 and set the role to "Admin"
        if role_id == 1:
            role = "admin"
        elif role_id == 2:
            role = "Customer"
        else:
            role = None

        # Add custom claims (e.g., role_id) to the token payload
        if role:
            data['role_name'] = role

        return data


class UserSerializer(serializers.ModelSerializer):
    phone_no = serializers.CharField(write_only=True)
    role_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_no', 'role_name']

    def create(self, validated_data):
        # Extract the additional fields
        role_name = validated_data.pop('role_name')
        phone_no = validated_data.pop('phone_no')

        # Ensure the role exists
        try:
            role = Role.objects.get(name=role_name)
        except Role.DoesNotExist:
            raise serializers.ValidationError({"role_name": "Invalid role name"})

        # Create the user
        user = User.objects.create_user(**validated_data)

        # Create the UserProfile
        UserProfile.objects.create(user=user, role=role, phone_no=phone_no)

        return user

    def update(self, instance, validated_data):
        phone_no = validated_data.pop('phone_no', None)
        role_name = validated_data.pop('role_name', None)

        # Update User fields
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Update or create UserProfile
        user_profile, created = UserProfile.objects.get_or_create(user=instance)
        if phone_no:
            user_profile.phone_no = phone_no
        if role_name:
            try:
                role = Role.objects.get(name=role_name)
                user_profile.role = role
            except Role.DoesNotExist:
                raise serializers.ValidationError({"role_name": "Invalid role name"})
        user_profile.save()

        return instance

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    role_name = serializers.CharField(source='role.name')
    phone_no = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = ['user_id', 'first_name', 'last_name', 'username', 'email', 'role_name', 'phone_no']
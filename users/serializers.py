from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = UserProfile
        fields = ['role']

    def validate_role(self, value):
        if not Role.objects.filter(id=value.id).exists():
            raise serializers.ValidationError(f"Invalid pk '{value.id}' - object does not exist.")
        return value
        
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        role_id = profile_data.get('role')

        # Ensure the role exists
        try:
            role = Role.objects.get(id=role_id.id)
            print(role)
        except Role.DoesNotExist:
            raise serializers.ValidationError({"profile": {"role": [f"Invalid pk '{role_id}' - object does not exist."]}})

        # Create the user and associate the role
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, role=role)
        return user

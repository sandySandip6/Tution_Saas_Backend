from rest_framework import serializers
from .models import CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, max_length=20, min_length=8,  )
    class Meta: 
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'address']
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                phone_number=validated_data.get('phone_number', ''),
                address=validated_data.get('address', ''),
                password=validated_data['password']
        )
        return user
            
            
        
    
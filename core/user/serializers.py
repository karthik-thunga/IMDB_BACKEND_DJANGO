from rest_framework import serializers
from core.user.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':"password"}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(detail="Passwords do not match")
        return data
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
           'last_name', 'email',
           'is_active', 'created', 'updated']
        read_only_field = ['is_active']
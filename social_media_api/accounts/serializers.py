from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()  
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'password', 'followers_count', 'following_count')
        extra_kwargs = {
            'password': {'write_only': True},  
        }

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()
    
    def create(self, validated_data):
        
        password = validated_data.pop('password')
        
        
        user = get_user_model().objects.create(**validated_data)
        
        
        user.set_password(password)
        user.save()
        
        
        Token.objects.create(user=user)
        
        return user

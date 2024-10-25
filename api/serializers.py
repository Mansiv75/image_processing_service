from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Image



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','email']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True}}
    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user       

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields=['id', 'image', 'user', 'uploaded_at']
        read_only_fields=['user','uploaded_at']        
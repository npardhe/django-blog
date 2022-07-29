from pyexpat import model
from re import L
from django.contrib.auth.models import User


from attr import field
from .models import Post,Profile,Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title','title_tag','author','body','category','snippet','header_image']
        def create(self,validated_data):
            return User.objects.create(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['user','bio','pinterest_url','website_url','facebook_url','twitter_url','instagram_url']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email','password']
        def create(self,validated_data):
            return User.objects.create(**validated_data)
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
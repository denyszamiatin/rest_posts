from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Posts


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email'


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = 'user', 'title', 'body'

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, PostsSerializer
from .models import Posts


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

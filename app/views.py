from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import User, Post, Comment, Favorite
from .serializers import (
    UserSerializer,
    PostSerializer,
    CommentSerializer,
    FavoriteSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import User, Post, Comment, Favorite
from .serializers import (
    UserSerializer,
    PostSerializer,
    CommentSerializer,
    FavoriteSerializer,
)


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ["name", "password"]


class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
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

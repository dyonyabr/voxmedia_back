from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from .models import User, Post, Comment, Favorite


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "user_name",
            "post",
            "content",
            "likes",
            "upload_time",
            "upload_date",
        ]

    def get_user_name(self, obj):
        return obj.user.name


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ["id", "user", "post"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source="comment_set")

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "description",
            "content",
            "likes",
            "comments",
            "upload_time",
            "upload_date",
        ]


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True, source="post_set")
    favorites = FavoriteSerializer(many=True, read_only=True, source="favorite_set")

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "password",
            "avatar",
            "posts",
            "favorites",
            "creation_time",
            "creation_date",
        ]

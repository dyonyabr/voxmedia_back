from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet, PostViewSet, CommentViewSet, FavouriteViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("favorites", FavouriteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

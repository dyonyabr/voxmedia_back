from django.contrib import admin

from .models import User, Post, Comment, Favorite


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    fields = ["name", "password", "avatar", "creation_date", "creation_time"]


@admin.register(Post)
class AdminUser(admin.ModelAdmin):
    fields = ["description", "likes", "content", "user", "upload_date", "upload_time"]


@admin.register(Comment)
class AdminUser(admin.ModelAdmin):
    fields = ["user", "post", "content", "likes", "upload_date", "upload_time"]


@admin.register(Favorite)
class AdminUser(admin.ModelAdmin):
    fields = ["user", "post"]

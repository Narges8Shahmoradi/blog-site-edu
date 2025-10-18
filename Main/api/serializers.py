from rest_framework import serializers
from ..models import Post, Category, Profile, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = [
            'user',
            'phone_number',
            'birth_date',
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'name',
            'email',
            'body',
            'created',
            'updated',
            'active',
        ]

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source='comments.all')
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'slug',
            'author',
            'publish',
            'created',
            'status',
            'comments',  # لیست کامنت‌ها
            'comments_count',  # تعداد کامنت‌ها
        ]

    def get_comments_count(self, obj):
        return obj.comments.count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
        ]
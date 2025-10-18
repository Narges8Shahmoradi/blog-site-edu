from rest_framework import serializers
from ..models import Post, Category, Profile, Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = [
            'user',
            'phone_number',
            'birth_date',
        ] 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        comment = serializers.CharField(source='Comment.all()')
        fields = [
           'title',
           'body',
           'author',
           'publish',
           'created',
           'status',
        ]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_name',
        ]
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'name',
            'email',
            'body',
            'created',
            'updated',
            'active',
        ]             
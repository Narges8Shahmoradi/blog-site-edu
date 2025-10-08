from rest_framework import serializers
from models import Post, Category

class UserSerializers(serializers.ModelSerializer):
    pass

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
           'tilte',
           'body',
           'author',
           'publish',
           'created',
           'status',
        ]

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_name',
        ]
               
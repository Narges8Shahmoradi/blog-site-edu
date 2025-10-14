from rest_framework import serializers
from ..models import Post, Category, Profile

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'phone_number',
            'birth_date',
        ]
        
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
               
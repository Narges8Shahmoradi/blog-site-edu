from rest_framework import serializers
from ..models import Post, Category, Profile

class UserSerializer(serializers.ModelSerializer):
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
        fields = [
           'tilte',
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
               
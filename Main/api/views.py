from rest_framework import viewsets
from ..models import Post, Category, Profile
from .serializers import PostSerializer, CategorySerializer, ProfileSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
#class CommentViewSet(viewsets.ModelViewSet):
 #   queryset = Comment.objects.all()
  #  serializer_class = CommentSerializer
  
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
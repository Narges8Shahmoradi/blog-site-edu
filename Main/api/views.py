from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import Post, Category, Profile, Comment
from .serializers import (PostSerializer,
                          CategorySerializer,
                          ProfileSerializer, 
                          CommentSerializer)

from .permissions import (IsAdminOrReadOnly, 
                          IsCommentOwnerOrAdmin,
                          IsOwnerOrAdmin, 
                          IsAuthorOrReadOnly)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdmin, IsAuthorOrReadOnly]
    
class CommentViewSet(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
   def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [AllowAny]  #anybody can do GET & POST with AllowAny
        else:
            permission_classes = [IsCommentOwnerOrAdmin]
        return [perm() for perm in permission_classes]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrAdmin, IsAdminOrReadOnly]
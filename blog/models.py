from django.db import models
from django.urls import reverse
from django.utils import timezone




class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date= 'publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=20, null=True, blank=True)
        
    def __str__(self):
        return self.category_name   
        

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    post_titles = [post.title for post in posts]
    return HttpResponse(f"List of Posts: {', '.join(post_titles)}")

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(f"Error: Post with ID {pk} not found.", status=404)
    return HttpResponse(f"Post Detail Page: Title: {post.title} | ID: {post.pk}")
from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404


# Create your views here


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'sports/post/list.html', {'posts': posts})


def post_details(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'sports/post/detail.html', {'post': post})

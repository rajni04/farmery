from django.shortcuts import render
from django.views.generic import CreateView
from post.models import Post
# Create your views here.


class AddPostView(CreateView):
    model=Post
    template_name='Blog/post.html'
    fields='__all__'

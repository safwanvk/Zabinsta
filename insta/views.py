from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from insta.models import Post


class PostListView(ListView):
    template_name = "insta/post_list.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'

from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView

from insta.models import Post


class PostListView(ListView):
    template_name = 'insta/home.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'

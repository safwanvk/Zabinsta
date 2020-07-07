from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView

from insta.models import Post


class PostListView(ListView):
    template_name = 'insta/home.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'insta/post_detail.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now())

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)
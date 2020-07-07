from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from insta.forms import PostForm
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


class PostCreateView(CreateView):
    template_name = 'insta/create.html'
    form_class = PostForm
    queryset = Post.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    template_name = 'insta/create.html'
    form_class = PostForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)


class PostDeleteView(DeleteView):
    template_name = 'insta/delete.html'

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('insta:post_list')
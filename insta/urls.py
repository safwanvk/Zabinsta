from django.contrib.auth.decorators import login_required
from django.urls import path

from insta.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostLikeAPIToggle, \
    PostLikeToggle

app_name = 'insta'

urlpatterns = [

    path('', login_required(PostListView.as_view()), name='post_list'),
    path('detail/<int:id>', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('update/<int:id>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:id>/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:id>/likes/', PostLikeToggle.as_view(), name='like_toggle'),
    path('api/<int:id>/likes/', PostLikeAPIToggle.as_view(), name='like_api_toggle'),
]

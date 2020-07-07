
from django.urls import path

from insta.views import PostListView, PostDetailView, PostCreateView, PostUpdateView

app_name = 'insta'

urlpatterns = [

    path('', PostListView.as_view(), name='post_list'),
    path('detail/<int:id>', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('update/<int:id>/', PostUpdateView.as_view(), name='post_update'),
]
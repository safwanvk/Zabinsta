
from django.urls import path

from insta.views import PostListView, PostDetailView

app_name = 'insta'

urlpatterns = [

    path('', PostListView.as_view(), name='post_list'),
    path('detail/<int:id>', PostDetailView.as_view(), name='post_detail'),
]
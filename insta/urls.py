
from django.urls import path

from insta.views import PostListView

app_name = 'insta'

urlpatterns = [

    path('', PostListView.as_view(), name='post_list')
]
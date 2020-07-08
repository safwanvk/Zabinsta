from django.contrib.auth.decorators import login_required
from django.urls import path, include

from accounts import views
from accounts.views import register_view

app_name = 'accounts'

urlpatterns = [
    path('register', register_view, name='register'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('profile/<str:username>', login_required(views.Profile.as_view()), name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]
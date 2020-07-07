from django.urls import path, include

from accounts.views import register_view

app_name = 'accounts'

urlpatterns = [
    path('register', register_view, name='register'),
    path('', include('django.contrib.auth.urls'), name='login')

]
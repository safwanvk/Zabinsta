from django.urls import path

from accounts.views import register_view

app_name = 'accounts'

urlpatterns = [
    path('', register_view, name='register')

]
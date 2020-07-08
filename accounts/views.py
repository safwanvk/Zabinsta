from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView

from . forms import UserCreationForm


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
    return render(request, 'accounts/register.html', {'form': form})


class Profile(DetailView):
    template_name = 'accounts/profile.html'
    queryset = User.objects.all()
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        # print(request.user)
        # print(user.profile.followed_by.all()[0])
        # print(type(user.profile.followed_by.all()[0]))
        return user

    def get_context_data(self, *args, **kwargs):
        context = super(Profile, self).get_context_data(*args, **kwargs)
        # user_id = self.kwargs.get('id')
        # user = get_object_or_404(User,id=user_id)
        user = self.get_object()
        context.update({
            'posts': user.posts.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
        })
        return context



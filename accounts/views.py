from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView
from .models import Profile as ProfileModel


from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


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

    def add_follow(self, request):
        user = self.get_object()
        user.profile.followed_by.add(request.user.profile)


def edit_profile(request):
    if request.method == "POST":

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'Your account has been updated successfully!')
            return redirect('insta:post_list')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/edit_profile.html', context)


class ProfileFollowAPIToggle(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, id=None, format=None):

        # id_ = self.kwargs.get("id")
        profile_obj = get_object_or_404(User, id=id)
        # url_ = profile_obj.get_absolute_url()
        user = self.request.user
        updated = False
        follow = False
        if user.is_authenticated:
            if user.profile in profile_obj.profile.followed_by.all():
                follow = False
                print(user.profile, "is un following ", profile_obj.profile)
                profile_obj.profile.followed_by.remove(user.profile)
            else:
                follow = True
                print(user.profile, "is following ", profile_obj.profile)
                profile_obj.profile.followed_by.add(user.profile)
            updated = True
        data = {
            "updated": updated,
            "follow": follow,
            "list": profile_obj.profile.followed_by.all().values("name"),
        }
        print(data)
        return Response(data)




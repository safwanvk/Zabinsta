from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse

from . forms import UserCreationForm


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
    return render(request, 'accounts/register.html', {'form': form})
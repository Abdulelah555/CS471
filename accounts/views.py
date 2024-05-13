from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UpdateNameForm

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


@login_required
def update_name(request):
    if request.method == 'POST':
        form = UpdateNameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('myprofile')
    else:
        form = UpdateNameForm(instance=request.user)
    return render(request, 'registration/update_name.html', {'form': form})
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (
TemplateView,
FormView,
RedirectView,
CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, SigninForm
from django.contrib.auth.models import User

class HomeView(TemplateView):
    template_name = 'users/home.html'

class Login(FormView):
    form_class = LoginForm
    template_name = 'users/includes/partials/login.html'
    success_url = reverse_lazy('dashboard:dashboard')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(Login, self).form_valid(form)
        else:
            return self.form_invalid(form)

class Logout(RedirectView):
    url = reverse_lazy('users:home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)

class Signin(CreateView):
    form_class = SigninForm
    model = User
    template_name = 'users/includes/partials/signin.html'
    success_url = reverse_lazy('dashboard:dashboard')

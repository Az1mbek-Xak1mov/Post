from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from authentication.forms import RegisterModelForm, LoginModelForm


# Create your views here.

class AuthTemplateView(TemplateView):
    template_name = 'authentication/login.html'


class RegisterFormView(FormView):
    form_class = RegisterModelForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error[0])
        return super().form_invalid(form)


class LoginFormView(FormView):
    form_class = LoginModelForm
    template_name = 'authentication/login.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.user
        login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('login')

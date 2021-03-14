from django.shortcuts import render
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'windex.html'


class LoginView(TemplateView):
    template_name = 'login.html'

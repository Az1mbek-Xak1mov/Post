from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, FormView

from app.forms import AuthorFormModel, PostFormModel, PostFilterForm
from app.models import Post, Author, Category


# Create your views here.

class HomeTemplateView(LoginRequiredMixin,ListView):
    model               = Post
    template_name       = 'app/home.html'
    context_object_name = 'posts'
    login_url = 'auth/login'
    def get_queryset(self):
        qs = super().get_queryset()
        self.filter_form = PostFilterForm(self.request.GET)
        if self.filter_form.is_valid():
            title = self.filter_form.cleaned_data.get('title')
            if title:
                qs = qs.filter(title__icontains=title)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        return context


class PostCreateView(CreateView):
    model         = Post
    form_class    = PostFormModel
    template_name = "app/new_post.html"
    success_url   = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['categories'] = Category.objects.all()
        return context


class AuthorFormView(CreateView):
    queryset =Author.objects.all()
    template_name = 'app/add-author.html'
    form_class = AuthorFormModel
    success_url = reverse_lazy('authors')

class AuthorListView(ListView):
    model = Author
    template_name = 'app/authors.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.annotate(num_posts=Count('posts'))

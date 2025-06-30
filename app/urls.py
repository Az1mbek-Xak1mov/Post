from django.urls import path

from app.views import HomeTemplateView, AuthorFormView, PostCreateView, AuthorListView

urlpatterns = [
    path('', HomeTemplateView.as_view(),name='home'),
    path('author_form', AuthorFormView.as_view(),name='author-form'),
    path('new_post', PostCreateView.as_view(),name='new_post'),
    path('authors', AuthorListView.as_view(),name='authors'),
]
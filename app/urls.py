from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app.views import reviewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='app/home.html'), name='home'),
    path('home', TemplateView.as_view(template_name='app/home.html'), name='home'),
    path('review', reviewView, name='review'),
    path('about', TemplateView.as_view(template_name='app/about-us.html'), name='about'),
]

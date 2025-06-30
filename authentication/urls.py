from django.urls import path

from authentication.views import LoginFormView, RegisterFormView, AuthTemplateView, logout_view

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('register', RegisterFormView.as_view(), name="register"),
    path('login', LoginFormView.as_view(), name="login"),
]

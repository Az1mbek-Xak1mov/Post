
from django.urls import path

from authenticate.views import LoginFormView

urlpatterns = [
    path('login' , LoginFormView.as_view() , name="login"),
]

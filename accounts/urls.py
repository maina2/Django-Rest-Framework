from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="user"),
    path("login/",views.LoginView.as_view(),name="login")
]

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="user"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("jwt/create/",TokenObtainPairView.as_view(),name="jwt_create"),
    path("jwt/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("jwt/verify",TokenVerifyView.as_view(),name="token_verify")
]

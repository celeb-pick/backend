from django.urls import path
from . import views

urlpatterns = [
    path('auth/status/', views.auth_status),
    path('login/', views.login),
    path('signup/', views.Signup.as_view()),
]

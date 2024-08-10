from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth),
    path('login/', views.login),
    path('signup/', views.Signup.as_view()),
]

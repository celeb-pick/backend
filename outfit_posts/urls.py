from django.urls import path
from . import views

urlpatterns = [
    path('outfit-posts/', views.OutfitPostList.as_view()),
]
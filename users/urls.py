from django.urls import path
from . import views

urlpatterns = [
    path('users/me/', views.MyProfileDetail.as_view()),
    path('users/me/outfit-posts/', views.MyOutfitPostList.as_view()),
    path('users/me/outfit-posts/scraps/', views.MyOutfitPostScrapList.as_view()),
    path('users/me/outfit-items/scraps/', views.MyOutfitItemScrapList.as_view()),
]

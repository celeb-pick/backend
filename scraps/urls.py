from django.urls import path
from . import views

urlpatterns = [
    path('outfit-posts/<int:outfit_post_id>/scraps/', views.OutfitPostScrapDetail.as_view()),
    path('outfit-items/<int:outfit_item_id>/scraps/', views.OutfitItemScrapDetail.as_view()),
]

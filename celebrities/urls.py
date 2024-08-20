from django.urls import path
from . import views

urlpatterns = [
    path('celebrities/', views.CelebrityList.as_view()),
]
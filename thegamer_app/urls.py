from django.urls import path, include
from thegamer_app import views

urlpatterns = [
    path('games', views.get_games),
    path('developers', views.get_developers),
    path('genres', views.get_genres),
    path('publishers', views.get_publishers),
    path('posts', views.get_posts),
]

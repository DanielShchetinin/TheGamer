from django.urls import path, include
from thegamer_app import views

urlpatterns = [
    path('games', views.get_games),
    path('games/<int:game_id>', views.get_game),
    path('games/<int:game_id>/developers', views.game_developers),

    path('developers', views.get_developers),
    path('developers/<int:developer_id>', views.get_developer),

    path('genres', views.get_genres),
    path('genres/<int:genre_id>', views.get_genre),

    path('publishers', views.get_publishers),
    path('publishers/<int:publisher_id>', views.get_publisher),

    path('posts', views.get_posts),
    path('posts/<int:post_id>', views.get_post),
]

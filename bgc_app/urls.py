"""Defines URL patterns for bgc_app."""
from django.urls import path
from . import views
app_name = 'bgc_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Board Game page
    path('games/', views.games, name='games'),
    # Details of a game
    path('details/<int:game_id>/', views.details, name='details'),
    # Page for adding a board game
    path('new_game/', views.new_game, name='new_game'),
    # Page for adding new details
    path('new_detail/<int:game_id>/', views.new_detail, name='new_detail'),
    # Page for editing details
    path('edit_detail/<int:detail_id>/', views.edit_detail, name='edit_detail'),
    # Page for editing a game
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
]

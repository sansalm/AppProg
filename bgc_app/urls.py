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
]

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Games

def index(request):
    """The home page for Board Game Club."""
    return render(request, 'bgc_app/index.html')

@login_required
def games(request):
    """Show all games."""
    games = Games.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'bgc_app/games.html', context)

@login_required
def details(request, game_id):
    """Show a single game and all its details."""
    game = Games.objects.get(id=game_id)
    details = game.details_set.order_by('-date_added')
    context = {'game': game, 'details': details}
    return render(request, 'bgc_app/details.html', context)

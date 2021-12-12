from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Games, Details
from .forms import GamesForm, DetailsForm

from django.http import Http404


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

@login_required
def new_game(request):
    """Add a new game."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GamesForm()
    else:
        # POST data submitted; process data.
        form = GamesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bgc_app:games')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'bgc_app/new_game.html', context)

@login_required
def new_detail(request, game_id):
    """Add a new game."""
    game = Games.objects.get(id=game_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = DetailsForm()
    else:
        # POST data submitted; process data.
        form = DetailsForm(data=request.POST)
        if form.is_valid():
            new_detail = form.save(commit=False)
            new_detail.game = game
            form.save()
            return redirect('bgc_app:details', game_id=game_id)
    # Display a blank or invalid form.
    context = {'game' : game, 'form': form}
    return render(request, 'bgc_app/new_detail.html', context)

@login_required
def edit_detail(request, detail_id):
    """Edit existing details"""
    detail = Details.objects.get(id=detail_id)
    game = detail.game
    
    if detail.game.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current details.
        form = DetailsForm(instance=detail)
    else:
        # POST data submitted; process data.
        form = DetailsForm(instance=detail, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bgc_app:details', game_id=game.id)

    context = {'detail' : detail, 'game' : game, 'form': form}
    return render(request, 'bgc_app/edit_detail.html', context)


@login_required
def edit_game(request, game_id):
    """Edit a game."""
    game = Games.objects.get(id=game_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GamesForm(instance=game)
    else:
        # POST data submitted; process data.
        form = GamesForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bgc_app:games')
    # Display a blank or invalid form.
    context = {'game': game, 'form': form}
    return render(request, 'bgc_app/edit_game.html', context)

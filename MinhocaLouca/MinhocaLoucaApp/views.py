from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'MinhocaLoucaApp/home.html')

def game(request):
    return render(request, 'MinhocaLoucaApp/game.html')

def leaderboard(request):
    return render(request, 'MinhocaLoucaApp/leaderboard.html')
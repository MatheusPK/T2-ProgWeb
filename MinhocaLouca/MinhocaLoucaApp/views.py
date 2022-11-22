from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def home(request):
    return render(request, 'MinhocaLoucaApp/home.html')

def game(request):
    return render(request, 'MinhocaLoucaApp/game.html')

class Login(LoginView):
    template_name='MinhocaLoucaApp/login.html'
    
def leaderboard(request):
    return render(request, 'MinhocaLoucaApp/leaderboard.html')

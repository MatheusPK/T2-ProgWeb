from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'MinhocaLoucaApp/home.html')

def game(request):
    return render(request, 'MinhocaLoucaApp/game.html')

class Login(LoginView):
    template_name='MinhocaLoucaApp/login.html'

class Logout(LogoutView):
    next_page=reverse_lazy('home')
    
def leaderboard(request):
    return render(request, 'MinhocaLoucaApp/leaderboard.html')

def signUp(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()
        context = {'form': formulario,}
        return render(request,'MinhocaLoucaApp/signup.html', context)

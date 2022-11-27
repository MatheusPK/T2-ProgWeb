from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.urls.base import reverse_lazy
from MinhocaLoucaApp.models import EasyScore, NormalScore, HardScore

# Create your views here.

def home(request):
    return render(request, 'MinhocaLoucaApp/home.html')

def game(request):
    return render(request, 'MinhocaLoucaApp/game.html')

class Login(LoginView):
    template_name='MinhocaLoucaApp/login.html'

class Logout(LogoutView):
    next_page=reverse_lazy('home')

def indexScores(scores): # labels ordered scores index
    list = []
    i = 0
    currentScore = 1000000 # greater than max possible score
    for score in scores:
        if score.score < currentScore:
            i += 1
        currentScore = score.score
        list.append({'value': score, 'i': str(i) + 'º'})
    return list
    
class Leaderboard(View):
    def get(self, request, *args, **kwargs):
        easyScores = EasyScore.objects.all().order_by('-score')
        normalScores = NormalScore.objects.all().order_by('-score')
        hardScores = HardScore.objects.all().order_by('-score')

        context = {
            'easyScores'   : indexScores(easyScores),
            'normalScores' : indexScores(normalScores),
            'hardScores'   : indexScores(hardScores)
        }

        return render(request, 'MinhocaLoucaApp/leaderboard.html', context)

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

def saveScore(request):
    # print(request.method)
    scorePoints = request.GET.get("score", None)
    username = request.GET.get("username", None)
    difficulty = request.GET.get("difficulty", None)

    if difficulty == "easy":
        score = EasyScore()
    elif difficulty == "normal":
        score = NormalScore()
    elif difficulty == "hard":
        score = HardScore()
    else:
        return
    
    score.username = username
    score.score = scorePoints
    score.save()
    return


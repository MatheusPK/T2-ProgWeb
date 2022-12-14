from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from MinhocaLoucaApp.models import EasyScore2, NormalScore2, HardScore2

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
        currentDiff = request.GET.get("difficulty", None)

        easyScores = EasyScore2.objects.all().order_by('-score')
        normalScores = NormalScore2.objects.all().order_by('-score')
        hardScores = HardScore2.objects.all().order_by('-score')
        print(easyScores)

        context = {
            'easyScores'   : indexScores(easyScores),
            'normalScores' : indexScores(normalScores),
            'hardScores'   : indexScores(hardScores),
            'currentDiff'  : currentDiff
        }

        return render(request, 'MinhocaLoucaApp/leaderboard.html', context)

def signUp(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        formulario = UserCreationForm()
        context = {'form': formulario,}
        return render(request,'MinhocaLoucaApp/signup.html', context)
    else:
        formulario = UserCreationForm()
        context = {'form': formulario,}
        return render(request,'MinhocaLoucaApp/signup.html', context)

def editAccount(request):
    if request.method == 'POST':
        newUsername = request.POST.get("newUsername")
        if request.user.is_authenticated:
            updatedUser = request.user
            updatedUser.username = newUsername
            updatedUser.save()
    return redirect('home')

def deleteAccount(request):
    username = request.GET.get("username", None)

    if User.objects.filter(username=username).exists():
        User.objects.get(username=username).delete()

    return redirect('home')

def saveScore(request):
    if not request.user.is_authenticated:
        return

        
    scorePoints = request.GET.get("score", None)
    username = request.GET.get("username", None)
    difficulty = request.GET.get("difficulty", None)

    if difficulty == "easy":
        score = EasyScore2()
    elif difficulty == "normal":
        score = NormalScore2()
    elif difficulty == "hard":
        score = HardScore2()
    else:
        return
    
    if request.user.is_authenticated:
        score.player = request.user
        score.score = scorePoints
        score.save()

    return


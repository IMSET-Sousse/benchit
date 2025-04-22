from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, BenchmarkForm
from .models import BenchmarkResult

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

@login_required
def home_view(request):
    if request.method == 'POST':
        form = BenchmarkForm(request.POST)
        if form.is_valid():
            benchmark = form.save(commit=False)
            benchmark.user = request.user
            benchmark.score = calculate_score(
                benchmark.cpu, benchmark.gpu, benchmark.ram, benchmark.storage
            )
            benchmark.save()
            return redirect('leaderboard')
    else:
        form = BenchmarkForm()
    return render(request, 'home.html', {'form': form})

def leaderboard_view(request):
    scores = BenchmarkResult.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'scores': scores})

def calculate_score(cpu, gpu, ram, storage):
    cpu_score = {'i3': 50, 'i5': 70, 'i7': 90, 'r5': 75, 'r7': 95}
    gpu_score = {'gtx1050': 60, 'gtx1660': 80, 'rtx3060': 100, 'integrated': 40}
    ram_score = {'8': 60, '16': 80, '32': 100}
    storage_score = {'hdd': 50, 'ssd': 90}
    
    total = (
        cpu_score.get(cpu, 0) +
        gpu_score.get(gpu, 0) +
        ram_score.get(ram, 0) +
        storage_score.get(storage, 0)
    ) / 4
    return total
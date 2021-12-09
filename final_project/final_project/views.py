from django.shortcuts import render
from .forms import CreatePollForm

def home(request):
    context = {}
    return render(request, 'quiz/Home.html', context)

def create(request):
    context = {}
    return render(request, 'quiz/Create.html', context)

def results(request):
    context = {}
    return render(request, 'quiz/Results.html', context)

def vote(request):
    context = {}
    return render(request, 'quiz/Vote.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'quiz/Create.html', context)
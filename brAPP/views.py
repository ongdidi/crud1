from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    input = request.GET["input"]
    computer = random.randint(1,3)
    if computer ==1:
        computer == "rock"
    elif computer ==2:
        computer = "scissors"
    else: 
        computer = "paper"
    return render(request, 'result.html', {'you':input, 'com' :computer})
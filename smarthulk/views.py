from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import timer
import time
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, "index.html") 

def meditation(request):
    return render(request, "meditation.html")

def emotion(request):
    return render(request, "emotion_detection.html")

def diary(request):
    return render(request, "diary.html")

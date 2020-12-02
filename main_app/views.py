from django.shortcuts import render
from django.http import HttpResponse

# return HttpResponse('<h1>It works!<h1>')

# --- STATIC PAGES
def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

# --- PROFILE PAGES
def showProfile(request):
    return HttpResponse('<h1>It Works!!!<h1>')

def profileIndex(request):
    return HttpResponse('<h1>It Works!!!<h1>')

def addProfile(request):
    return HttpResponse('<h1>It Works!!!<h1>')

# --- POST PAGES

# --- AUTH 
def signup(request):
    return HttpResponse('<h1>It Works!!!<h1>')

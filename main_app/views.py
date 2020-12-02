from django.shortcuts import render
from django.http import HttpResponse

# return HttpResponse('<h1>It works!<h1>')

# --- STATIC PAGES
def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

# --- USER PAGES

# --- POST PAGES

# --- AUTH 

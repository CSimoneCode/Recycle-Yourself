from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, SignupForm
from django.http import HttpResponse

# return HttpResponse('<h1>It works!<h1>')

# --- STATIC PAGES
def landing(request):
    return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')


def donorInfo(request):
    return HttpResponse('<h1>It works!<h1>')


def recipientInfo(request):
    return HttpResponse('<h1>It works!<h1>')


# --- PROFILE PAGES
def showProfile(request, user_id):
    profile = Profile.objects.get(user=user_id)

    context = {
        'profile': profile,
        }

    return render(request, 'profile/show.html', context)


def profileIndex(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}

    return render(request, 'profile/index.html', context)


def addProfile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user_id = request.user.id
            new_profile.save()
            return redirect('showProfile', new_profile.user_id)
        else:
            error_message = 'Something went wrong - try again'
    else:
        profile_form = ProfileForm()
        context = {
            'profile_form': profile_form, 
            'error_message': error_message
        }
        return render(request, 'profile/add.html', context)

@login_required
def editProfile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            edited_profile = profile_form.save()
            return redirect('showProfile')
        else:
            error_message = 'Something went wrong - try again'
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'profile_form': profile_form, 
            'error_message': error_message
        }
        return render(request, 'profile/edit.html', context)


@login_required
def deleteProfile(request):
    error_message = ''
    if request.method == 'POST':
        Profile.objects.get(id=request.user.profile.id).delete()
        return redirect('landing')
    else:
        error_message = 'Something went wrong - try again'
        return redirect('showProfile')

# --- POST PAGES

# --- AUTH 
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            new_email = user.email
            if User.objects.filter(email=new_email):
                error_message = 'Email already exists'
            else:
                user = form.save()
                login(request, user)
                return redirect('addProfile')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignupForm()
    context = {
        'form': form, 
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)

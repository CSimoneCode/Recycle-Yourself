from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Post
from .forms import ProfileForm, SignupForm, PostForm
from django.http import HttpResponse

# return HttpResponse('<h1>It works!<h1>')

#----------------------------------------------------------------------------------------------
#           STATIC
#----------------------------------------------------------------------------------------------
def landing(request):
    return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')


def donorInfo(request):
    profile = Profile.objects.filter(account_type='DN')
    posts = Post.objects.select_related().filter(author__in=profile,  public=True)
    context = { 'posts': posts }
    return render(request, 'donorInfo.html', context)


def recipientInfo(request):
    profile = Profile.objects.filter(account_type='RC')
    posts = Post.objects.select_related().filter(author__in=profile, public=True)
    context = { 'posts': posts }
    return render(request, 'recipientInfo.html', context)


#----------------------------------------------------------------------------------------------
#           PROFILES
#----------------------------------------------------------------------------------------------
def showProfile(request, user_id):
    profile = Profile.objects.get(user=user_id)
    user = Profile.objects.select_related().get(user=user_id)
    posts = Post.objects.filter(author=user_id)

    context = {
        'profile': profile,
        'posts': posts,
        'user': user,
        }

    return render(request, 'profile/show.html', context)


def profileIndex(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}

    return render(request, 'profile/index.html', context)


def addProfile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
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
def myProfile(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author=request.user.id)
    context = {
        'profile': profile,
        'posts': posts,
        }

    return render(request, 'profile/show.html', context)


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
        Profile.objects.get(user=request.user).delete()
        return redirect('landing')
    else:
        error_message = 'Something went wrong - try again'
        return render(request, 'showProfile')


#----------------------------------------------------------------------------------------------
#           POSTS
#----------------------------------------------------------------------------------------------
def showPost(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
    'post': post,
    }

    return render(request, 'post/show.html', context)


@login_required
def addPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author_id = request.user.id
            new_post.save()
            return redirect('showPost', new_post.id)
    else:
        post_form = PostForm()
        author = request.user
        context = {
            'post_form': post_form,
            'author': author,
        }
        return render(request, 'post/add.html', context)


@login_required
def deletePost(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('recipientInfo')


@login_required
def editPost(request, post_id):
    found_post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=found_post)
        if post_form.is_valid():
            updated_post = post_form.save()
            return redirect('showPost', updated_post.id)
    else:
        post_form = PostForm(instance=found_post)
        context = {
            'post': found_post,
            'post_form': post_form
        }
        return render(request, 'post/edit.html', context)


#----------------------------------------------------------------------------------------------
#           AUTH
#----------------------------------------------------------------------------------------------
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

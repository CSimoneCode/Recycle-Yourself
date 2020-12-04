# URL configuration for recycle_yourself
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # ----- STATIC
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('donorInfo/', views.donorInfo, name='donorInfo'),
    path('recipientInfo', views.recipientInfo, name='recipientInfo'),
    # ----- PROFILE
    path('profile/index/', views.profileIndex, name='profileIndex'),
    path('profile/addProfile/', views.addProfile, name='addProfile'),
    path('profile/<int:user_id>/', views.showProfile, name='showProfile'),
    path('profile/myProfile/', views.myProfile, name='myProfile'),
    # path('profile/<int:user_id>/edit', views.editProfile, name='editProfile'),
    # ----- POST
    path('post/add/', views.addPost, name='addPost'),
    path('post/<int:post_id>/', views.showPost, name='showPost'),
    path('post/<int:post_id>/edit', views.editPost, name='editPost'),

    # ----- AUTH
    path('registration/signup/', views.signup, name='signup')
]
    
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
    # path('profile/<int:user_id>/edit', views.editProfile, name='editProfile'),
    # ----- POST

    # ----- AUTH
    path('registration/signup/', views.signup, name='signup')
]
    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField(blank=True)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    location = models.CharField(max_length=80)
    bio = models.CharField(max_length=500)
    account_type = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

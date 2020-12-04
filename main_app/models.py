from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    DONOR = 'DN'
    RECIPIENT = 'RC'
    CHAMPION = 'CH'
    ACCOUNT_TYPE_CHOICES = [
        (DONOR, 'Donor'),
        (RECIPIENT, 'Recipient'),
        (CHAMPION, 'Champion'),
    ]
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField(blank=True)
    photo = models.ImageField(default='user.png', upload_to='profile_pics', blank=True)
    location = models.CharField(max_length=80)
    bio = models.CharField(max_length=500)
    account_type = models.CharField(
        max_length=9,
        choices=ACCOUNT_TYPE_CHOICES,
        default=CHAMPION)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(default='default.jpg', upload_to='post_pics', blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

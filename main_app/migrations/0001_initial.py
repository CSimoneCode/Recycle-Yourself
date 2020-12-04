# Generated by Django 3.1.4 on 2020-12-02 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('date_of_birth', models.DateField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('location', models.CharField(max_length=80)),
                ('bio', models.CharField(max_length=500)),
                ('account_type', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

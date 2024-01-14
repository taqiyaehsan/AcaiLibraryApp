from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Library(models.Model):
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    page_count = models.IntegerField()
    category = models.CharField(max_length=50)
    shelf_location = models.CharField(max_length=50)
    published_date = models.DateField()
    is_in_stock = models.BooleanField(default=True)
    date_checked_out = models.DateField(null=True, blank=True)

class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [('Admin', 'Admin'), ('User', 'User')]
    role = models.CharField(max_length=50, choices=role_choices)

    def __str__(self):
        return self.user.username
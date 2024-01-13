# library_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Library, UserProfile
from faker import Faker
import random
from datetime import datetime, timedelta, timezone
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

fake = Faker()

def populate_library_data(request):
    # Generate and populate 200 entries with random data
    for _ in range(200):
        Library.objects.create(
            publisher=fake.company(),
            author=fake.name(),
            title=fake.catch_phrase(),
            page_count=random.randint(50, 1000),
            category=fake.word(),
            shelf_location=fake.word(),
            published_date=fake.date_between(start_date='-10y', end_date='today'),
            is_in_stock=random.choice([True, False]),
            date_checked_out=fake.date_between(start_date='-1y', end_date='today') if random.choice([True, False]) else None,
        )

    libraries = Library.objects.all()
    return render(request, 'library_app/library_list.html', {'libraries': libraries})

def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library_app/library_list.html', {'libraries': libraries})

def user_list(request):
    # if request.user.userprofile.role != 'Admin':
        # return render(request, 'library_app/access_denied.html')
    
    users = UserProfile.objects.all()
    return render(request, 'library_app/user_list.html', {'users': users})
    
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a UserProfile instance associated with the new user
            user_profile = UserProfile.objects.create(user=user, role='User')

            login(request, user)
            return redirect('home')  # Redirect to the home page or another page
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL you want to redirect after login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')
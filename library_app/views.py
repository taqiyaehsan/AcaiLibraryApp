# library_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library, UserProfile
from faker import Faker
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import random
from datetime import datetime, timedelta, timezone
from rest_framework import generics, status
from rest_framework.response import Response
from django.views import View
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

fake = Faker()

class PopulateLibraryDataView(View):
    def get(self, request, *args, **kwargs):
        libraries = Library.objects.all()
        response_content = render(request, 'library_app/library_list_htmx.html', {'libraries': libraries})
        return HttpResponse(response_content)

class LibraryListView(View):
    def get(self, request, *args, **kwargs):
        libraries = Library.objects.all()
        response_content = render(request, 'library_app/library_list_htmx.html', {'libraries': libraries})
        # response_content = render(request, 'library_app/library_list_js.html', {'libraries': libraries})
        return HttpResponse(response_content)

class UserListView(View):
    def dispatch(self, request, *args, **kwargs):
        # Check if the user has the "admin" role
        if not request.user.is_authenticated or request.user.userprofile.role != 'Admin':
            return HttpResponse("Access Denied. You do not have permission to access this page.", status=403)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        users = UserProfile.objects.all()
        response_content = render(request, 'library_app/user_list.html', {'users': users})
        return HttpResponse(response_content)

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            # Create a UserProfile instance associated with the new user
            role = form.cleaned_data['role']
            user_profile = UserProfile.objects.create(user=user, role=role)
            login(request, user)
            return redirect('user-dashboard')  
        
        return render(request, 'registration/register.html', {'form': form})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user-dashboard') 
        return render(request, 'registration/login.html', {'form': form})
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')  # Redirect to the login page after logout

def home_view(request):
    return render(request, 'home.html')

def user_dashboard_view(request):
    return render(request, 'user_dash.html', {'user': request.user})
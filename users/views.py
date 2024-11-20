from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Profile

# Home View
class HomeView(LoginRequiredMixin, View):
    login_url = '/login/' 

    def get(self, request):
        return render(request, 'home.html')
    
# Register View
class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.username = form.cleaned_data['email']
            user.save()
            Profile.objects.create(user=user)
            login(request, user)  
            return redirect('home')  
        return render(request, 'register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        profile, created  = Profile.objects.get_or_create(user=request.user)
        
        profile_form = ProfileUpdateForm(instance=profile)

        return render(request, 'profile.html', {
            'profile_form': profile_form
        })

    
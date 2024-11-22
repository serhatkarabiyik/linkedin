from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm
from skills.forms import SkillForm
from experience.forms import ExperienceForm
from .models import Profile
from posts.models import Post
from skills.models import Skill
from experience.models import Experience

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


# Profile View
class ProfileView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, user_id=None):
        if user_id is None:  
            user = request.user
        else:
            user = get_object_or_404(User, id=user_id)

        profile, created = Profile.objects.get_or_create(user=user)
        profile_form = ProfileUpdateForm(instance=profile)

        posts = Post.objects.filter(user=user).order_by('-created_at')

        skills = profile.skills.all()
        skill_form = SkillForm()

        can_edit = profile.user == request.user

        experiences = Experience.objects.filter(user=user)
        experience_form = ExperienceForm()

        suggested_users = User.objects.exclude(id=user.id)


        return render(request, 'profile.html', {
            'profile_form': profile_form,
            'posts': posts,
            'user': user,
            'skills': skills,
            'skill_form': skill_form,
            'experiences': experiences,
            'experience_form': experience_form,
            'suggested_users': suggested_users,
            'can_edit': can_edit,
        })

    def post(self, request, user_id=None):
        if user_id:
            profile = Profile.objects.get(user__id=user_id)
        else:
            profile = request.user.profile
        profile_form = ProfileUpdateForm(request.POST, instance=profile)

        skill_form = SkillForm(request.POST)

        if skill_form.is_valid():
            new_skill = skill_form.cleaned_data.get('new_skill')
            existing_skill = skill_form.cleaned_data.get('existing_skills')

            if new_skill:
                new_skill_obj, created = Skill.objects.get_or_create(name=new_skill)
                profile.skills.add(new_skill_obj) 

            if existing_skill:
                profile.skills.add(existing_skill)

            return redirect('profile', user_id=profile.user.id)

        to_user = get_object_or_404(User, id=user_id)

        if to_user != request.user:
            ConnectionRequest.objects.create(from_user=request.user, to_user=to_user)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')

        return render(request, 'profile.html', {
            'profile_form': profile_form,
            'skills': profile.skills.all(),
            'skill_form': skill_form,
            'can_edit': profile.user == request.user,
        })

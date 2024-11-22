from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from users.models import Profile
from reaction.models import Reaction
import os
from django.conf import settings

class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'  

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        user_posts_count = Post.objects.filter(user=request.user).count()

        suggested_users = Profile.objects.exclude(id=request.user.id)

        context = {
            'posts': posts,
            'user_posts_count': user_posts_count,
            'suggested_users': suggested_users,
        }

        return render(request, 'home.html', context)

    def post(self, request):
        content = request.POST.get('content')
        picture_file = request.FILES.get('picture')

        if picture_file:
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'img')
            os.makedirs(upload_dir, exist_ok=True)

            file_path = os.path.join(upload_dir, picture_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in picture_file.chunks():
                    destination.write(chunk)

            picture_url = f'img/{picture_file.name}'
        else:
            picture_url = None

        if content:
            Post.objects.create(
                user=request.user,
                content=content,
                picture=picture_url
            )
            return redirect('home')

        posts = Post.objects.all().order_by('-created_at')
        error_message = "Le contenu du post ne peut pas être vide."
        return render(request, 'home.html', {'posts': posts, 'error_message': error_message})


class DeletePostView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        if post.user != request.user:
            raise Http404("Vous n'êtes pas autorisé à supprimer ce post.")

        post.delete() 
        return redirect('profile')

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from posts.models import Post

class AddCommentView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        
        content = request.POST.get('content')
        if not content:
            return redirect('home')  

        comment = Comment.objects.create(
            user=request.user,
            post=post,
            content=content
        )
        
        return redirect('home') 



class DeleteCommentView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.user != request.user:
            return HttpResponseForbidden("Vous n'avez pas l'autorisation de supprimer ce commentaire.")

        comment.delete()
        return redirect('home')
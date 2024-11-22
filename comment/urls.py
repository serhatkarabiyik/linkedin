from django.urls import path
from .views import AddCommentView, DeleteCommentView

urlpatterns = [
    path('add_comment/<int:post_id>/', AddCommentView.as_view(), name='add_comment'),
    path('delete_comment/<int:comment_id>/', DeleteCommentView.as_view(), name='delete_comment'),
]

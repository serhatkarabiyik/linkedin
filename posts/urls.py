from django.urls import path
from .views import HomeView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/delete/<int:post_id>/', DeletePostView.as_view(), name='delete_post'),
]


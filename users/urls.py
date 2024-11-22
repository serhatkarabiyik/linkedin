from django.urls import path, include
from .views import RegisterView, ProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/', include('skills.urls')),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
]

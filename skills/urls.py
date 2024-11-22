from django.urls import path
from .views import SkillView

urlpatterns = [
    path('', SkillView.as_view(), name='skills'),
]

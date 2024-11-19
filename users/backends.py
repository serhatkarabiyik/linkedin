from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    """
    Authentifie l'utilisateur via son email au lieu de son nom d'utilisateur.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        except Exception as e:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

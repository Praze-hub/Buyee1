from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed


class CustomBackend(ModelBackend):
    """Allowa sign with email or password"""

    def authenticate(self, request, **kwargs):
        UserModel = get_user_model()
        try:
            username = kwargs.get(UserModel.USERNAME_FIELD, None)
            password = kwargs.get("password", None)

            if username is None or password is None:
                return None
            if user := UserModel.objects.filter(Q(email__iexact=username)).first():
                if user.is_active and user.check_password(password):
                    return user
            raise AuthenticationFailed(
                "You have entered an invalid phone number/email address or password")
        except UserModel.DoesNotExist:
            return None

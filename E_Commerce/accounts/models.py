from django.db import models
from django.contrib.auth.base_user import BaseUserManager

import uuid
from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
# from helpers.models import TrackingModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
import jwt
from datetime import datetime, timedelta
from django.conf import settings


class CustomUserManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields, ):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    username = models.CharField('username', max_length=150, unique=True,
                                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                validators=[username_validator],
                                error_messages={'unique': "A user with that username already exists."}, )

    email = models.EmailField('email_address', blank=False, unique=True)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.', )
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    email_verified = models.BooleanField('email_verified',
                                         default=False,
                                         help_text='Designates whether this seers email is verified',
                                         )

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)

    def save_last_login(self):
        self.last_login = datetime.now()
        self.save()

    @property
    def token(self):
        token = jwt.encode({'username': self.username, 'email': self.email,
                            'exp': datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY,
                           algorithm='HS256')
        return token

    class Meta:
        ordering = ("-created_at",)

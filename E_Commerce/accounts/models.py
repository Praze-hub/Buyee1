from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from uuid import uuid4
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager




class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering  = ("-created",)
    
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user  = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("SuperUser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("SuperUser must have is_superuser = True"))
        
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    email= models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email


    

        



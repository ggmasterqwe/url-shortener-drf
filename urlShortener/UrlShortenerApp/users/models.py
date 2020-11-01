from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that uses email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        
        self.set_password(self.password)

        return super().save(*args,**kwargs)


from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('This object requires an email')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, password):

        user = self.create_user(email, password)
        user.is_staff = True

        user.is_superuser = True
        user.save(using=self._db)
        return user

import binascii
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
""" Custom UserManager """
class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


""" Custom User model """
class User(AbstractBaseUser):
    objects = UserManager()
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    def get_full_name(self):
    # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
    # The user is identified by their email address
        return self.email

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
    # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
    # Simplest possible answer: Yes, always
        return True

    def is_staff(self):
    # Simplest possible answer: All admins are staff
        return self.is_admin
from datetime import datetime
import datetime
from hashlib import sha256
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# from django.contrib.auth.models import AbstractBaseUser, UserManager

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "NewUser",
        on_delete=models.SET_DEFAULT,
        default=None,
        to_field="id"
    )

    def __str__(self):
        return self.title

class Run(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    distance = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "NewUser",
        on_delete=models.SET_DEFAULT,
        default=None,
        to_field="id"
    )

    def __str__(self):
        return self.title

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError("You must provide an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must be assigned to is_staff=True."
            )
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True."
            )

        return self.create_user(email, username, first_name, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    about = models.TextField(_("about"), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "password"]

    def __str__(self):
        return self.username


# class User(AbstractBaseUser):
#     objects = UserManager()

#     def create_superuser(self, username, email, password):
#         return self._create_user(username, email, password)

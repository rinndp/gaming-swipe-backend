import secrets
import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from email_validator import validate_email as validate, EmailNotValidError

from favgames.models.favgame_model import FavGame


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        try:
            valid = validate(email)
            email = valid.normalized
        except EmailNotValidError as e:
            raise ValueError(str(e))

        if CustomUser.objects.filter(email=email).exists():
            raise ValueError('Email already registered.')

        if password and len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email = email, password = password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, null=False, blank=False, unique=True, verbose_name="Username")
    google_id = models.CharField(max_length=70, null=True, blank=True, verbose_name="Google ID")
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True, verbose_name="Email")
    favorite_games = models.ManyToManyField(FavGame, related_name="favorited_by", blank=True)
    played_games = models.ManyToManyField(FavGame, related_name="played_by", blank=True)
    image = models.ImageField(upload_to="profile_images", null=True, blank=True, verbose_name="Profile image")
    slug = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name="Slug")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    is_staff = models.BooleanField(default=False, verbose_name="Staff")
    is_subscribed = models.BooleanField(default=False, verbose_name="Subscribed")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.email} - {self.username}"


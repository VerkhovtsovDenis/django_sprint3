from django.db import models
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    """Модель базы данных для объекта Публикация."""

    pass


class Category(models.Model):
    """Модель базы данных для объекта Тематическая категория."""

    pass


class Location(models.Model):
    """Модель базы данных для объекта Географическая метка."""

    pass


class User(AbstractUser):
    """Модель базы данных для объекта Пользователь."""

    pass

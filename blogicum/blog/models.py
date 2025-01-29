"""This module is described db Models."""

from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ForeignKey, \
    BooleanField, SlugField
from django.contrib.auth import get_user_model


# Модель базы данных для объекта Пользователь
User = get_user_model()


class Category(models.Model):
    """Модель базы данных для объекта Тематическая категория."""

    title = CharField(max_length=256, blank=False)
    description = TextField(blank=False)
    slug = SlugField(unique=True, blank=False)
    is_published = BooleanField(default=True, blank=False)
    created_at = DateTimeField(auto_created=True, blank=False)

    pass


class Location(models.Model):
    """Модель базы данных для объекта Географическая метка."""

    name = CharField(max_length=256, blank=False)
    is_published = BooleanField(default=True, blank=False)
    created_at = DateTimeField(auto_created=True, blank=False)

    pass


class Post(models.Model):
    """Модель базы данных для объекта Публикация."""

    title = CharField(max_length=256, blank=False)
    text = TextField(blank=False)
    pub_date = DateTimeField(blank=False)
    author = CharField(max_length=256, blank=False)
    author = ForeignKey(User, on_delete=models.CASCADE,
                        related_name='fk_publications')
    location = ForeignKey(Location, on_delete=models.SET_NULL, blank=True)
    is_published = BooleanField(default=True, blank=False)
    created_at = DateTimeField(auto_created=True, blank=False)

    pass

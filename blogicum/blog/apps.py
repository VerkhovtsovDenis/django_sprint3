"""This module describes Blog app."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Класс-конфигурации приложения Blog."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Блог'

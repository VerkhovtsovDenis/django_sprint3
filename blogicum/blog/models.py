"""This module is described db Models."""

from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ForeignKey, \
    BooleanField, SlugField
from django.contrib.auth import get_user_model


# Модель базы данных для объекта Пользователь
User = get_user_model()


class Category(models.Model):
    """Модель базы данных для объекта Тематическая категория."""

    title = CharField(max_length=256, blank=False, verbose_name='Заголовок')
    description = TextField(blank=False, verbose_name='Описание')
    slug = SlugField(
                     unique=True,
                     blank=False,
                     verbose_name='Идентификатор',
                     help_text='Идентификатор страницы для URL; разрешены \
символы латиницы, цифры, дефис и подчёркивание.')

    is_published = BooleanField(
                                default=True,
                                blank=False,
                                verbose_name='Опубликовано',
                                help_text='Снимите галочку, \
чтобы скрыть публикацию.'
    )
    created_at = DateTimeField(
                               blank=False,
                               verbose_name='Добавлено',
                               auto_now_add=True
    )

    class Meta:
        """Зарещенный на територии РФ класс, \
        описывающий наименование модели объекта на Рус. яз."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Возвращает заголовок тематической категории."""
        return self.title


class Location(models.Model):
    """Модель базы данных для объекта Географическая метка."""

    name = CharField(
                     max_length=256,
                     blank=False,
                     verbose_name='Название места'
    )
    is_published = BooleanField(
                                default=True,
                                blank=False,
                                verbose_name='Опубликовано'
    )
    created_at = DateTimeField(
                               blank=False,
                               verbose_name='Добавлено',
                               auto_now_add=True
    )

    class Meta:
        """Зарещенный на територии РФ класс, \
        описывающий наименование модели объекта на Рус. яз."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        """Возвращает наименование георагафической метки."""
        return self.name


class Post(models.Model):
    """Модель базы данных для объекта Публикация."""

    title = CharField(max_length=256, blank=False, verbose_name='Заголовок')
    text = TextField(blank=False, verbose_name='Текст')
    pub_date = DateTimeField(
                             blank=False,
                             verbose_name='Дата и время публикации',
                             help_text='Если установить дату и время в \
будущем — можно делать отложенные публикации.'
    )
    author = ForeignKey(
                        User,
                        on_delete=models.CASCADE,
                        related_name='fk_author',
                        blank=False,
                        verbose_name='Автор публикации'
    )
    location = ForeignKey(
                          Location,
                          on_delete=models.SET_NULL,
                          related_name='fk_location',
                          blank=False,
                          null=True,
                          verbose_name='Местоположение'
    )
    category = ForeignKey(
                          Category,
                          on_delete=models.SET_NULL,
                          related_name='fk_category',
                          blank=False,
                          null=True,
                          verbose_name='Категория'
    )
    is_published = BooleanField(
                                default=True,
                                blank=False,
                                verbose_name='Опубликовано'
    )
    created_at = DateTimeField(
                               auto_created=True,
                               blank=False,
                               verbose_name='Добавлено',
                               auto_now_add=True
    )

    class Meta:
        """Зарещенный на територии РФ класс, \
        описывающий наименование модели объекта на Рус. яз."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        """Возвращает заголовок публикации."""
        return self.title

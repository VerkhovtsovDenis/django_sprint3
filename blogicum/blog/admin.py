from django.contrib import admin

from .models import Category, Post, Location, User

# ...и регистрируем её в админке:
admin.site.register([Category, Post, Location])

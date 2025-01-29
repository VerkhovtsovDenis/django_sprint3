from django.contrib import admin

from .models import Category, Post, Location, User

admin.site.register([Category, Post, Location])

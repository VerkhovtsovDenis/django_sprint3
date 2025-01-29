"""This module describes admin-panel configuration of Blog app."""

from django.contrib import admin

from .models import Category, Post, Location

admin.site.register([Category, Post, Location])

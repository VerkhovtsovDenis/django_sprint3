"""This module is described routing functions (control in MVC model)."""

from django.shortcuts import render
from django.http import Http404
from blog.models import Post, Category, Location


def index(request):
    template = 'blog/index.html'
    context = {
        'post_list': Post.objects.all()
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'

    post = Post.objects.get(id=post_id)

    # Если пост не найден, вызываем ошибку 404
    if post is None:
        raise Http404(f"Post with {post_id=} does not exist")

    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    category_id = Category.objects.get(slug=category_slug).id
    filtered_posts = Post.objects.filter(category=category_id)

    context = {
        'category': category_slug,
        'post_list': filtered_posts
    }

    return render(request, template, context)

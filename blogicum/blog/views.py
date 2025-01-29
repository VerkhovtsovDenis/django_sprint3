"""This module is described routing functions (control in MVC model)."""

from django.shortcuts import render
from blog.models import Post, Category
from datetime import datetime
from django.shortcuts import get_object_or_404


def index(request):
    """Возвращает главную страницу с инфрормацией о 5 записях."""
    template = 'blog/index.html'

    published_category = Category.objects.filter(is_published=True)
    today = datetime.today().date()

    context = {
        'post_list': Post.objects.filter(
                                         pub_date__lte=today,
                                         is_published=True,
                                         category__in=published_category
        )[:5]
    }
    return render(request, template, context)


def post_detail(request, post_id):
    """Возвращает страницу с постом по его id."""
    template = 'blog/detail.html'

    published_category = Category.objects.filter(is_published=True)

    today = datetime.today().date()
    post = get_object_or_404(
                             Post,
                             id=post_id,
                             is_published=True,
                             pub_date__lte=today,
                             category__in=published_category
           )

    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    """Возвращает страницу категории по её slug."""
    template = 'blog/category.html'

    today = datetime.today().date()

    category_id = get_object_or_404(Category,
                                    slug=category_slug,
                                    is_published=True).id
    filtered_posts = Post.objects.filter(
                                         category=category_id,
                                         pub_date__lte=today,
                                         is_published=True
    )

    context = {
        'category': category_slug,
        'post_list': filtered_posts
    }

    return render(request, template, context)

from django.shortcuts import render
from django.http import Http404


def index(request):
    template = 'blog/index.html'
    context = {
        'posts': posts[::-1]
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'

    # Поиск поста по id
    post = posts_dict.get(post_id)

    # Если пост не найден, вызываем ошибку 404
    if post is None:
        raise Http404(f"Post with {post_id=} does not exist")

    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    filtered_posts = [post for post in posts
                      if post['category'] == category_slug]

    context = {
        'category': category_slug,
        'posts': filtered_posts
    }

    return render(request, template, context)

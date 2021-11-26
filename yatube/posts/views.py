from django.shortcuts import get_object_or_404, render

from .models import Group, Post

RANGE_POSTS = 10


def index(requests):
    posts = Post.objects.all()[:RANGE_POSTS]
    template = 'posts/index.html'
    main_page = "Последние обновления на сайте"
    context = {
        'main_page': main_page,
        'posts': posts,
    }
    return render(requests, template, context)


def group_posts(requests, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = group.posts.all()[:RANGE_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(requests, template, context)

from .models import Post, Group
from django.shortcuts import render, get_object_or_404


def index(requests):
    posts = Post.objects.order_by('-pub_date')[:10]
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
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(requests, template, context)

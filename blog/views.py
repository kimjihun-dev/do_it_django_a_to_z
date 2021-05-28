from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        # 기존에 제공했던 기능을 가져와 context 담는다
        context = super(PostList, self).get_context_data()
        # 모든 카테고리를 가져와 categories 에 담는다
        context['categories'] = Category.objects.all()
        # 카테고리가 지정되지 않은 포스트의 갯수를 카운팅하여 담는다
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'post_list': post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'category': category
    }
    return render(request, 'blog/post_list.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    context = {
        'post_list': post_list,
        'tag:': tag,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count()
    }
    return render(request, 'blog/post_list.html', context)


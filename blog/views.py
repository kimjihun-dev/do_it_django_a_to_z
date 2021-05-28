from django.views.generic import ListView, DetailView
from .models import Post, Category


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

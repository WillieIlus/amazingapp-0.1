from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogList(ListView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/list.html'


class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/detail.html'
    count_hit = True

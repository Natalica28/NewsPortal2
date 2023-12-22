from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .forms import PostForm
from .filters import PostFilter

class PostList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'one_news'

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_choice = 'NW'
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def get_queryset(self):
        return Post.objects.filter(post_choice='NW')

class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    raise_exception = True
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(post_choice='NW')

class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_art',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_choice = 'AR'
        return super().form_valid(form)

class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'

    def get_queryset(self):
        return Post.objects.filter(post_choice='AR')

class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    raise_exception = True
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(post_choice='AR')
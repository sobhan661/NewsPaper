from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


from .models import Article


class ArticlesList(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles_list.html"
    context_object_name = "articles"


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = [
        "title",
        "body",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"


class ArticleEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = [
        "title",
        "body",
    ]
    template_name = "article_edit.html"
    context_object_name = "article"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("articles_list")
    template_name = "article_delete.html"
    context_object_name = "article"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

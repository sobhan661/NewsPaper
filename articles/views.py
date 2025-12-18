from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from .models import Article


class ArticlesList(ListView):
    model = Article
    template_name = "articles_list.html"
    context_object_name = "articles"


class ArticleCreate(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = [
        "title",
        "author",
        "body",
    ]


class ArticleDetail(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"


class ArticleEdit(UpdateView):
    model = Article
    fields = [
        "title",
        "body",
    ]
    template_name = "article_edit.html"
    context_object_name = "article"


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy("articles_list")
    template_name = "article_delete.html"
    context_object_name = "article"

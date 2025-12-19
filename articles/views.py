from django.views.generic import (
    ListView,
    DetailView,
    FormView,
)
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views import View
from django.views.generic.detail import SingleObjectMixin


from .models import Article
from .forms import CommentForm


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


class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleDetail(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


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

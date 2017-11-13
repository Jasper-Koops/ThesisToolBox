from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from source_tracker.models import Book, Pamphlet, Article
from source_tracker.forms import BookForm, PamphletForm, ArticleForm
from notes.views import BaseNoteCreateView

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        data = super(Home, self).get_context_data(**kwargs)
        data['books'] = Book.objects.filter(user=self.request.user)
        data['pamphlets'] = Pamphlet.objects.filter(user=self.request.user)
        data['articles'] = Article.objects.filter(user=self.request.user)
        return data

    template_name = "source_tracker/source_tracker_home.html"


class BookCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = BookForm
    template_name = "source_tracker/book_create.html"
    success_url = reverse_lazy('source_tracker_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Book
    form_class = BookForm
    template_name = 'base/generic_form.html'
    success_url = reverse_lazy('source_tracker_home')


class BookDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Book
    template_name = 'source_tracker/detail_views/book_detail.html'


class BookNoteAdd(BaseNoteCreateView):
    pass


class PamphletCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = PamphletForm
    template_name = "source_tracker/pamphlet_create.html"
    success_url = reverse_lazy('source_tracker_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PamphletUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Pamphlet
    form_class = PamphletForm
    template_name = 'base/generic_form.html'
    success_url = reverse_lazy('source_tracker_home')


class PamphletDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Pamphlet
    template_name = 'source_tracker/detail_views/pamphlet_detail.html'


class PamphletNoteAdd(BaseNoteCreateView):
    pass


class ArticleCreate(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = "source_tracker/article_create.html"
    success_url = reverse_lazy('source_tracker_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'base/generic_form.html'
    success_url = reverse_lazy('source_tracker_home')


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'source_tracker/detail_views/article_detail.html'


class ArticleNoteAdd(BaseNoteCreateView):
    pass


class SourceNoteAdd(BaseNoteCreateView):
    template_name = "base/generic_form.html"
    success_url = reverse_lazy('source_tracker_home')

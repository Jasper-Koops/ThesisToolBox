from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from source_tracker.models import Book, Pamphlet, Article
from source_tracker.forms import BookForm, PamphletForm, ArticleForm
from notes.views import BaseNoteCreateView

# Create your views here.

class Home(TemplateView):

    def get_context_data(self, **kwargs):
        data = super(Home, self).get_context_data(**kwargs)
        data['books'] = Book.objects.all()
        data['pamphlets'] = Pamphlet.objects.all()
        data['articles'] = Article.objects.all()
        return data

    template_name = "source_tracker/source_tracker_home.html"


class BookCreate(CreateView):
    form_class = BookForm
    template_name = "source_tracker/book_create.html"
    success_url = reverse_lazy('source_tracker_home')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'base/generic_form.html'
    success_url = reverse_lazy('source_tracker_home')


class BookDetail(DetailView):
    model = Book
    template_name = 'source_tracker/detail_views/book_detail.html'


class BookNoteAdd(BaseNoteCreateView):
    pass


class PamphletCreate(CreateView):
    form_class = PamphletForm
    template_name = "source_tracker/pamphlet_create.html"
    success_url = reverse_lazy('source_tracker_home')


class PamphletUpdate(UpdateView):
    model = Pamphlet
    form_class = PamphletForm
    template_name = 'base/generic_form.html'
    success_url = reverse_lazy('source_tracker_home')


class PamphletDetail(DetailView):
    model = Pamphlet
    template_name = 'source_tracker/detail_views/pamphlet_detail.html'


class PamphletNoteAdd(BaseNoteCreateView):
    pass


class ArticleCreate(CreateView):
    form_class = ArticleForm
    template_name = "source_tracker/article_create.html"
    success_url = reverse_lazy('source_tracker_home')


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'base/generic_form.html'
    success_url = reverse_lazy('source_tracker_home')


class ArticleDetail(DetailView):
    model = Article
    template_name = 'source_tracker/detail_views/article_detail.html'


class ArticleNoteAdd(BaseNoteCreateView):
    pass


class SourceNoteAdd(BaseNoteCreateView):
    template_name = "base/generic_form.html"
    success_url = reverse_lazy('source_tracker_home')

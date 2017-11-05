from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from source_tracker.models import Book, Pamphlet, Article
from source_tracker.forms import BookForm, PamphletForm, ArticleForm

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


class PamphletCreate(CreateView):
    form_class = PamphletForm
    template_name = "source_tracker/pamphlet_create.html"
    success_url = reverse_lazy('source_tracker_home')


class ArticleCreate(CreateView):
    form_class = ArticleForm
    template_name = "source_tracker/article_create.html"
    success_url = reverse_lazy('source_tracker_home')
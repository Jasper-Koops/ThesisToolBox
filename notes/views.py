from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import NoteForm
from .models import Tag

from person_tracker.models import Person
from source_tracker.models import Book, Article, Pamphlet

from django.apps import apps

# Create your views here.

class BaseNoteCreateView(CreateView):

    form_class = NoteForm

    def get_form_kwargs(self):
        kwargs = super(BaseNoteCreateView, self).get_form_kwargs()
        kwargs['model'] = self.kwargs['model']
        kwargs['app'] = self.kwargs['app']
        kwargs['model_pk'] = self.kwargs['model_pk']
        return kwargs


class TagOverview(ListView):
    model = Tag
    template_name = 'notes/tag_overview.html'


class TagDetail(DetailView):
    model = Tag
    template_name = 'notes/tag_detail.html'

    def get_context_data(self, **kwargs):
        data = super(TagDetail, self).get_context_data(**kwargs)
        data['books'] = Book.objects.filter(tags=self.object)
        data['pamphlets'] = Pamphlet.objects.filter(tags=self.object)
        data['articles'] = Article.objects.filter(tags=self.object)
        return data


class TagCreate(CreateView):
    model = Tag
    template_name = 'base/generic_form.html'
    fields = ['name']
    success_url = reverse_lazy('tag_overview')

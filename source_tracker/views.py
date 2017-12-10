from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from source_tracker.models import Source
from source_tracker.forms import SourceForm
from notes.views import BaseNoteCreateView
from notes.utils import source_dict_generator

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        data = super(Home, self).get_context_data(**kwargs)
        data['sources'] =Source.objects.filter(user=self.request.user)
        return data

    template_name = "source_tracker/source_tracker_home.html"


class SourceCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = SourceForm
    template_name = "source_tracker/source_create.html"
    success_url = reverse_lazy('source_tracker_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReactBookCreate(LoginRequiredMixin, TemplateView):
    template_name = 'source_tracker/react_book_create.html'

class SourceUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Source
    form_class = SourceForm
    template_name = 'base/generic_form.html'
    success_url = reverse_lazy('source_tracker_home')


class SourceDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Source
    template_name = 'source_tracker/detail_views/source_detail.html'

    #Return a dict with the tag and its linked sources.
    def get_context_data(self, **kwargs):
        data = super(SourceDetail, self).get_context_data(**kwargs)
        linked_Tags = self.object.tags.filter(user=self.request.user)
        data['notes'] = source_dict_generator(linked_Tags, self)
        return data


class BookNoteAdd(BaseNoteCreateView):
    pass


class SourceNoteAdd(BaseNoteCreateView):
    template_name = "base/generic_form.html"
    success_url = reverse_lazy('source_tracker_home')

from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.forms.models import model_to_dict
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import NoteForm
from .models import Tag, Note

from person_tracker.models import Person
from source_tracker.models import Source

from django.apps import apps

# Create your views here.

class TodoView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'base/todo.html'

class BaseNoteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = NoteForm

    def get_form_kwargs(self):
        kwargs = super(BaseNoteCreateView, self).get_form_kwargs()
        kwargs['model'] = self.kwargs['model']
        kwargs['app'] = self.kwargs['app']
        kwargs['model_pk'] = self.kwargs['model_pk']
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TagOverview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Tag
    template_name = 'notes/tag_overview.html'

    def get_queryset(self):
        qs = Tag.objects.filter(user=self.request.user)
        return qs


class TagDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Tag
    template_name = 'notes/tag_detail.html'

    def get_context_data(self, **kwargs):
        data = super(TagDetail, self).get_context_data(**kwargs)

        returndict = {}
        linked_Sources = Source.objects.filter(
            tags__id=self.object.pk,
            user=self.request.user
        )

        for source in linked_Sources:
            hashed_source = model_to_dict(source)
            hashed_source['hashed_author'] = {
                'id': source.author.pk,
                'name': source.author.full_name,
            }
            dict_list = [hashed_source]
            notes = source.notes.filter(
                tags__id=self.object.pk,
                user=self.request.user
            )
            for note in notes:
                tag_list = []
                for tag in note.tags.all():
                    tag_list.append({
                        'id': tag.pk,
                        'name': tag.name
                    })
                dict_model = model_to_dict(note)
                dict_model['linked_tags'] = tag_list
                dict_list.append(dict_model)
            returndict[source] = dict_list

        data['notes'] = returndict
        return data


class TagCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Tag
    template_name = 'base/generic_form.html'
    fields = ['name']
    success_url = reverse_lazy('tag_overview')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TagNoteAdd(BaseNoteCreateView):
    template_name = "base/generic_form.html"
    success_url = reverse_lazy('tag_overview')

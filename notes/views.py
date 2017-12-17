from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .utils import tag_dict_generator
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
    model = Note
    fields = ['content', 'tags']

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.request.user
        self.model = self.kwargs['model']
        self.app = self.kwargs['app']
        print(self.app)
        self.key = self.kwargs['model_pk']
        self.model_object = apps.get_model(self.app, self.model)
        self.linked_object = self.model_object.objects.get(pk=self.key)
        form.instance.content_object = self.linked_object

        #check if tag is in linked object tags
        #Add tag if this is not the case.
        tags = form.cleaned_data['tags']

        #Tag objects cannot have tags, so skipp this part if the 'linked_object'
        #is a tag.
        if self.linked_object.__class__.__name__ == 'Tag':
            pass
        else:
            for tag in tags:
                if tag in self.linked_object.tags.all():
                    pass
                else:
                    self.linked_object.tags.add(tag)

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
        #Generate filtered dict with Sources as keys and the linked comments
        #as values.
        linked_Sources = Source.objects.filter(
            tags__id=self.object.pk,
            user=self.request.user
        )
        data['notes'] = tag_dict_generator(linked_Sources, self)
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

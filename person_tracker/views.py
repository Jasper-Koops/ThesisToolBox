from django.shortcuts import render
from django.apps import apps
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from person_tracker.models import Person, Nationality
from person_tracker.forms import PersonForm
from notes.views import BaseNoteCreateView



class Home(ListView):
    #template_name = "person_tracker/person_tracker_home.html"
    model = Person
    template_name = "person_tracker/person_overview.html"


class PersonOverview(ListView):
    model = Person
    template_name = "person_tracker/person_overview.html"


class PersonCreate(CreateView):
    model = Person
    success_url = reverse_lazy('person_overview')
    form_class = PersonForm
    template_name = "person_tracker/person_create.html"


class PersonDetail(DetailView):
    model = Person
    template_name = "person_tracker/person_detail.html"
    context_object_name = 'actor'

    # def get_context_data(self, **kwargs):
    #     data = super(PersonDetail, self).get_context_data(**kwargs)
    #     print(self.kwargs['pk'])
    #     current_person = Person.objects.get(self.kwargs['pk'])

        # return data


class PersonNoteAdd(BaseNoteCreateView):
    template_name = "person_tracker/generic_form.html"
    success_url = reverse_lazy('person_overview')


class PersonNoteUpdate():
    pass


class NationalityCreate(CreateView):
    model = Nationality
    success_url = reverse_lazy('person_overview')
    fields = ['name']
    template_name = "person_tracker/nationality_create.html"


class NationalityOverview(ListView):
    model = Person
    template_name = "person_tracker/nationality_overview.html"

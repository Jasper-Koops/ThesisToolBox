from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from person_tracker.models import Person, Nationality
from person_tracker.forms import PersonForm
# Create your views here.

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


class NationalityCreate(CreateView):
    model = Nationality
    success_url = reverse_lazy('person_overview')
    fields = ['name']
    template_name = "person_tracker/nationality_create.html"


class NationalityOverview(ListView):
    model = Person
    template_name = "person_tracker/nationality_overview.html"
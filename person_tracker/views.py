from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from person_tracker.models import Person, Nationality
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
    fields = ['firstname', 'middlename', 'lastname', 'year_of_birth', 'year_of_death', 'nationality', 'branch']
    template_name = "person_tracker/person_create.html"


class NationalityOverview(ListView):
    model = Person
    template_name = "person_tracker/nationality_overview.html"
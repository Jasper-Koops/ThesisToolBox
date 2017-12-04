from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from person_tracker.models import Person, Nationality
from person_tracker.forms import PersonForm
from notes.views import BaseNoteCreateView



class Home(LoginRequiredMixin, ListView):
    #template_name = "person_tracker/person_tracker_home.html"
    login_url = '/login/'
    model = Person
    template_name = "person_tracker/person_overview.html"

    def get_queryset(self):
        qs = Person.objects.filter(user=self.request.user)
        return qs


class PersonOverview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Person
    template_name = "person_tracker/person_overview.html"

    def get_queryset(self):
        qs = Person.objects.filter(user=self.request.user)
        return qs


class PersonCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Person
    success_url = reverse_lazy('person_overview')
    form_class = PersonForm
    template_name = "person_tracker/person_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PersonDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Person
    template_name = "person_tracker/person_detail.html"
    context_object_name = 'actor'


class PersonNoteAdd(BaseNoteCreateView):
    login_url = '/login/'
    template_name = "person_tracker/generic_form.html"
    success_url = reverse_lazy('person_overview')


class PersonNoteUpdate():
    login_url = '/login/'
    pass


class NationalityCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Nationality
    success_url = reverse_lazy('person_overview')
    fields = ['name']
    template_name = "person_tracker/nationality_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NationalityOverview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Person
    template_name = "person_tracker/nationality_overview.html"

    def get_queryset(self):
        qs = Person.objects.filter(user=self.request.user)
        return qs

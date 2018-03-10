from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Search


class SearchListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'hansardscraper/search_list.html'
    model = Search


class SearchDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/search_detail.html'
    model = Search

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Search, BlockQuote, Debate, Session, Speaker
from hansardscraper.tasks import perform_query


class SearchListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'hansardscraper/search_list.html'
    model = Search

    def post(self, request):
        text = self.request.POST.get('search-query', None)
        perform_query.delay(text)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class SearchDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/search_detail.html'
    model = Search


class QuoteDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/quote.html'
    model = BlockQuote


class DebateDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/debate_detail.html'
    model = Debate


class SessionDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/session_detail.html'
    model = Session


class SpeakerDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/speaker_detail.html'
    model = Speaker

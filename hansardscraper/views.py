from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Search, BlockQuote, Debate, Session, Speaker
from hansardscraper.tasks import perform_query
from notes.views import BaseNoteCreateView


class FavoriteNoteAdd(BaseNoteCreateView):
    template_name = "base/generic_form.html"
    success_url = reverse_lazy('scraper:favorites')


class FavoritesListView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'hansardscraper/favorites.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['quotes'] = BlockQuote.objects.filter(favorited=True)
        data['debates'] = Debate.objects.filter(favorited=True)
        return data


class SearchListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'hansardscraper/search_list.html'
    model = Search

    def post(self, request):
        text = self.request.POST.get('search-query', None)
        if text != None:
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

    def post(self, request, pk):
        item = self.get_object()
        item.favorited = True
        item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class DebateDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/debate_detail.html'
    model = Debate

    def post(self, request, pk):
        item = self.get_object()
        item.favorited = True
        item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class SessionDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/session_detail.html'
    model = Session


class SpeakerDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'hansardscraper/speaker_detail.html'
    model = Speaker

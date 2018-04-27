from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from notes.models import Note, Tag

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'ThesisToolBox/index.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        data = super(Index, self).get_context_data(**kwargs)
        data['notes'] = Note.objects.filter(user=self.request.user).order_by('-id')[:3]

        data['tags'] = Tag.objects.filter(user=self.request.user).order_by('-id')[:8]
        return data
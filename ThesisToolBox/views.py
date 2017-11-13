from django.views.generic import TemplateView
from source_tracker.models import Book, Article, Pamphlet
from person_tracker.models import Person
from notes.models import Note, Tag

class Index(TemplateView):
    template_name = 'ThesisToolBox/index.html'

    def get_context_data(self, **kwargs):
        data = super(Index, self).get_context_data(**kwargs)
        data['notes'] = Note.objects.all().order_by('-id')[:5]
        return data
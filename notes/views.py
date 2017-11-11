from django.views.generic import FormView, CreateView
from .forms import NoteForm
from django.apps import apps

# Create your views here.

class BaseNoteCreateView(CreateView):

    form_class = NoteForm

    def get_form_kwargs(self):
        kwargs = super(BaseNoteCreateView, self).get_form_kwargs()
        kwargs['model'] = self.kwargs['model']
        kwargs['app'] = self.kwargs['app']
        kwargs['model_pk'] = self.kwargs['model_pk']
        return kwargs


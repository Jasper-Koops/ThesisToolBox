from django.forms import ModelForm
from notes.models import Note
from django.apps import apps


class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model')
        self.app = kwargs.pop('app')
        self.key = kwargs.pop('model_pk')
        self.model_object = apps.get_model(self.app, self.model)
        self.linked_object = self.model_object.objects.get(pk=self.key)
        super(NoteForm, self).__init__(*args, **kwargs)


    def save(self, commit=True):
        note = super(NoteForm, self).save(commit=False)
        note.content_object = self.linked_object
        note.save()
        if commit:
            note.save()
        return note

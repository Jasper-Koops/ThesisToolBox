from .serializers import *
from source_tracker.models import Source
from notes.models import Note, Tag
from person_tracker.models import Person
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('-pk')
    serializer_class = PersonSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-pk')
    serializer_class = NoteSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('-pk')
    serializer_class = TagSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all().order_by('-publication_date')
    serializer_class = SourceSerializer


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer


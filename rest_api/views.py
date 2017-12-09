from .serializers import *
from source_tracker.models import Book, Pamphlet, Article
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


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-publication_date')
    serializer_class = BookSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-publication_date')
    serializer_class = ArticleSerializer


class PamphletViewSet(viewsets.ModelViewSet):
    queryset = Pamphlet.objects.all().order_by('-publication_date')
    serializer_class = PamphletSerializer


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer


from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from source_tracker.models import Book, Pamphlet, Article
from notes.models import Note, Tag
from person_tracker.models import Person
from rest_framework import permissions


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all().order_by('-pk')
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'api_note_detail'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-pk')
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'api_note_detail'
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-publication_date')
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'api_book_detail'
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookCreate(generics.CreateAPIView):
    serializer_class = ReactBookSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-publication_date')
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PamphletList(generics.ListCreateAPIView):
    queryset = Pamphlet.objects.all().order_by('-publication_date')
    serializer_class = PamphletSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PamphletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pamphlet.objects.all()
    serializer_class = PamphletSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    User = get_user_model()
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('api:api_book_list'),
        'articles': reverse('api:api_article_list'),
        'pamphlets': reverse('api:api_pamphlet_list'),
        'users': reverse('api:api_user_list'),
        'notes': reverse('api:api_note_list'),
        'persons': reverse('api:api_person_list'),
    })


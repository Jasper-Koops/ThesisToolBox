from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from source_tracker.models import Book, Pamphlet, Article
from rest_framework import permissions


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-publication_date')
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'api_book_detail'
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


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

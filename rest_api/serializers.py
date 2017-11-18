from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from source_tracker.models import Book, Pamphlet, Article
from notes.models import Note, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'email', 'groups')


class BookSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'added_on', 'source_type', 'publisher_name', 'publisher_city', 'user')




class PamphletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pamphlet
        fields = ('title', 'author', 'publication_date', 'added_on', 'user')



class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'author', 'publication_date', 'added_on', 'user')





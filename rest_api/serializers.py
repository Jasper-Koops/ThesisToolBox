from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from source_tracker.models import Book, Pamphlet, Article
from notes.models import Note, Tag
from person_tracker.models import Person


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('id', 'username', 'email', 'groups')



class NoteSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Note
        fields = ('id', 'added_on', 'content', 'object_id', 'user')



class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    notes = NoteSerializer(many=True)


    class Meta:
        model = Person
        fields = (
        'firstname', 'middlename', 'lastname', 'added_on', 'year_of_birth', 'year_of_death', 'branch', 'notes', 'user')



class BookSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    notes = NoteSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_date', 'added_on', 'source_type', 'publisher_name', 'publisher_city', 'user', 'notes')




class PamphletSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    notes = NoteSerializer(many=True)

    class Meta:
        model = Pamphlet
        fields = ('title', 'author', 'publication_date', 'added_on', 'notes', 'user')



class ArticleSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    notes = NoteSerializer(many=True)

    class Meta:
        model = Article
        fields = ('title', 'author', 'publication_date', 'added_on', 'notes', 'user')





from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from source_tracker.models import Source
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


class TagSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    notes = NoteSerializer(many=True)

    class Meta:
        model = Tag
        fields = ('id', 'added_on', 'name', 'notes', 'user')


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    notes = NoteSerializer(many=True)
    tags = TagSerializer(many=True)


    class Meta:
        model = Person
        fields = (
        'firstname', 'middlename', 'lastname', 'added_on', 'year_of_birth', 'year_of_death', 'branch', 'historian', 'notes', 'tags', 'user')



class SourceSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    notes = NoteSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Source
        fields = ('id', 'title', 'publication_date', 'added_on', 'source_type', 'source_class', 'publisher_name', 'publisher_city', 'user', 'notes', 'tags')



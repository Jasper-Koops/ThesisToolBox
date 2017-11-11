from django.forms import ModelForm, SelectDateWidget
from source_tracker.models import Book, Pamphlet, Article


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'publisher_name', 'publisher_city', 'source_type']
        widgets = {
            'publication_date': SelectDateWidget(years=range(1800, 2020)),
        }


class PamphletForm(ModelForm):

    class Meta:
        model = Pamphlet
        fields = ['title', 'author', 'publication_date']
        widgets = {
            'publication_date': SelectDateWidget(years=range(1800, 2020)),
        }


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'author', 'publication_date']
        widgets = {
            'publication_date': SelectDateWidget(years=range(1800, 2020)),
        }
from django.forms import ModelForm, SelectDateWidget
from source_tracker.models import Source


class SourceForm(ModelForm):

    class Meta:
        model = Source
        fields = ['title', 'author', 'publication_date', 'publisher_name', 'publisher_city', 'source_type', 'source_class', 'tags']
        widgets = {
            'publication_date': SelectDateWidget(years=range(1800, 2020)),
        }

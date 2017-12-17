from django.forms import ModelForm, SelectDateWidget
from person_tracker.models import Person, Nationality

class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['firstname', 'middlename', 'lastname', 'year_of_birth', 'year_of_death', 'nationality', 'branch', 'historian', 'tags']
        widgets = {
            'year_of_birth': SelectDateWidget(years=range(1800, 2018)),
            'year_of_death': SelectDateWidget(years=range(1800, 2018)),
        }

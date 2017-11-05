from django.forms import ModelForm, SelectDateWidget
from person_tracker.models import Person, Nationality

class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['firstname', 'middlename', 'lastname', 'year_of_birth', 'year_of_death', 'nationality', 'branch']
        widgets = {
            'year_of_birth': SelectDateWidget(),
            'year_of_death': SelectDateWidget(),
        }
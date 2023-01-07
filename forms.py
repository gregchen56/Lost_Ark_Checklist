from django.forms import ModelForm, CheckboxInput
from .models import Character, CharDaily

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = [
            'user',
            'char_name',
        ]

class CharDailyForm(ModelForm):
    class Meta:
        model = CharDaily
        fields = (
            "__all__"
        )

from typing import Any

from django.forms import DateTimeInput, ModelForm
from django.forms.fields import BooleanField

from mailings.models import Mailings


class StyleFormMixin:

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """ uniform style of form fields """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MailingsForm(StyleFormMixin, ModelForm):

    class Meta:
        """ Filling out the date and time form via the calendar """
        model = Mailings
        exclude = ('is_active', 'owner',)
        widgets = {
            'start_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

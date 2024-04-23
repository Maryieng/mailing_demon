from django.forms import ModelForm

from letters.models import Message
from mailings.forms import StyleFormMixin


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:
        """ card form when created """
        model = Message
        exclude = ('owner',)

from letters.models import Message
from mailings.forms import StyleFormMixin
from django.forms import ModelForm


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Message
        exclude = ('owner',)

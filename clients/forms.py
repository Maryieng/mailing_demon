from django.forms import ModelForm

from clients.models import Clients
from mailings.forms import StyleFormMixin


class ClientsForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Clients
        exclude = ('owner',)

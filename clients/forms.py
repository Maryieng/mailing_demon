from django.forms import ModelForm

from clients.models import Clients
from mailings.forms import StyleFormMixin


class ClientsForm(StyleFormMixin, ModelForm):

    class Meta:
        """ card form when created """
        model = Clients
        exclude = ('owner',)

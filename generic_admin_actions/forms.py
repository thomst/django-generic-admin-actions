from django import forms
from django.utils.translation import gettext_lazy as _


class GenericActionsForm(forms.Form):
    generic_action = forms.CharField(
        label=_('Generic Actions'),
    )

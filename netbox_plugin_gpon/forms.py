from django import forms
from django.urls import reverse
from utilities.forms import BootstrapMixin, SlugField, DynamicModelChoiceField, APISelect

from .models import *

from django.core.validators import RegexValidator


class OLTForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = OLT
        exclude = ('',)
from django import forms
from django.urls import reverse
from utilities.forms import BootstrapMixin, SlugField, DynamicModelChoiceField, APISelect

from .models import *

from django.core.validators import RegexValidator


class OLTForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = OLT
        exclude = ('',)

class GPONFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(
        required=False,
        label="Name",
    )

    site = forms.ModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        to_field_name="slug"
    )

    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        to_field_name="slug"
    )

    device_type = forms.ModelChoiceField(
        queryset=DeviceType.objects.all(),
        required=False,
        to_field_name="slug"
    )
class OLTFilterForm(GPONFilterForm):
    class Meta:
        model = OLT
        fields = []

class ONTFilterForm(GPONFilterForm):
    class Meta:
        model = ONT
        fields = []
class GPONSplitterFilterForm(GPONFilterForm):
    class Meta:
        model = GPONSplitter
        fields = []

class ONTForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = ONT
        fields = ('name', 'site', 'manufacturer', 'device_type', 'uplink','type', 'ip_address', 'comments')

class GPONSplitterForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = GPONSplitter
        fields = ('name', 'site', 'manufacturer', 'device_type','uplink_type', 'content_type', 'object_id', 'comments')
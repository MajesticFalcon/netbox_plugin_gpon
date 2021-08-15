import django_filters
from django.db.models import Q

from .models import *

class GPONFilterSet(django_filters.FilterSet):

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    site = django_filters.ModelMultipleChoiceFilter(
        field_name="site__slug",
        queryset=Site.objects.all(),
        to_field_name="slug",
    )

    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name="manufacturer__slug",
        queryset=Manufacturer.objects.all(),
        to_field_name="slug",
    )

    device_type = django_filters.ModelMultipleChoiceFilter(
        field_name="devicetype__slug",
        queryset=DeviceType.objects.all(),
        to_field_name="slug",
    )

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | Q(site__icontains=value)
        return queryset.filter(qs_filter)

class OLTFilterSet(GPONFilterSet):
    class Meta:
        model = OLT
        fields = [
            'name',

        ]

class ONTFilterSet(GPONFilterSet):
    class Meta:
        model = ONT
        fields = [
            'name',

        ]
class GPONSplitterFilterSet(GPONFilterSet):
    class Meta:
        model = GPONSplitter
        fields = [
            'name',
        ]
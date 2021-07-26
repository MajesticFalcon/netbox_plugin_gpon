import django_tables2 as tables
from django.urls import reverse
from django_tables2.utils import A  # alias for Accessor


from .models import *


from utilities.tables import (
    BaseTable,
    ButtonsColumn,
    ChoiceFieldColumn,
    TagColumn,
    ToggleColumn
)

class OLTTable(BaseTable):
    pk = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = OLT
        fields = ("pk", "name")


class GPONSplitterTable(BaseTable):
    pk = tables.LinkColumn()
    uplink_type = tables.Column(verbose_name="Splitter Type")
    class Meta(BaseTable.Meta):
        model = GPONSplitter
        fields = ("pk", "name", "uplink_type")

class ONTTable(BaseTable):
    pk = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = ONT
        fields = ("pk", "name", "uplink")
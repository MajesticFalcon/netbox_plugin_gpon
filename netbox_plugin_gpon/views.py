from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils import timezone
from utilities.views import GetReturnURLMixin

from netbox_plugin_gpon.netbox_plugin_gpon.views.generic import *
from . import forms



from .models import *
from . import tables

class OLTListView(ObjectListView, View):
    queryset = OLT.objects.all()
    table = tables.OLTTable

class OLTEditView(ObjectEditView, View):
    queryset = OLT.objects.all()
    model_form = forms.OLTForm

class OLTView(ObjectView):
    queryset = OLT.objects.all()

    def get(self, request, *args, **kwargs):
        current_olt = get_object_or_404(self.queryset, **kwargs)
        splitters = GPONSplitter.objects.filter(object_id=current_olt.pk)
        splitter_table = tables.GPONSplitterTable(splitters)
        RequestConfig(request, paginate={"per_page": 5}).configure(splitter_table)

        #outer_list=splitters
        #inner_list=nids
        #return a list of nids whose FK corresponds to one of the splitters linked to this OLT
        onts = [nid for splitter in splitters for nid in splitter.ont_set.all()]
        ont_table = tables.ONTTable(onts)
        #RequestConfig(request, paginate={"per_page": 25}).configure(ont_table)


        return render(
            request,
            self.get_template_name(),
            {
                "object": current_olt,
                "splitter_table": splitter_table,
                "splitter_count": len(splitters),
                "ont_table": ont_table,
                "ont_count": len(onts),

            },
        )

class GPONSplitterListView(ObjectListView, View):
    queryset = GPONSplitter.objects.all()
    table = tables.GPONSplitterTable

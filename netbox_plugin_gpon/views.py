from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils import timezone
from utilities.views import GetReturnURLMixin

from netbox_plugin_gpon.netbox_plugin_gpon.views.generic import *
from . import forms



from .models import *
from . import tables
from . import filters

class HomeView(View):
    template_name = "netbox_plugin_gpon/home.html"
    def get(self, request):
        olts = OLT.objects.all()
        olt_table = tables.OLTTable(olts)
        RequestConfig(request, paginate={"per_page": 20}).configure(olt_table)

        onts = ONT.objects.all()
        ont_table = tables.ONTTable(onts)
        RequestConfig(request, paginate={"per_page": 20}).configure(ont_table)

        gponsplitters = GPONSplitter.objects.all()
        gponsplitters_table = tables.GPONSplitterTable(gponsplitters)
        RequestConfig(request, paginate={"per_page": 20}).configure(gponsplitters_table)

        return render(request, self.template_name,{
            'olt_table': olt_table,
            'ont_table': ont_table,
            'gponsplitters_table': gponsplitters_table,
        })

class OLTListView(ObjectListView, View):
    alt_title="OLTs"
    queryset = OLT.objects.all()
    table = tables.OLTTable
    filterset = filters.OLTFilterSet
    filterset_form = forms.OLTFilterForm

class OLTEditView(ObjectEditView, View):
    alt_title = "OLT"
    queryset = OLT.objects.all()
    model_form = forms.OLTForm

class OLTView(ObjectView):
    alt_title = "OLT"
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

class ONTListView(ObjectListView, View):
    alt_title = "ONTs"
    queryset = ONT.objects.all()
    table = tables.ONTTable
    filterset = filters.ONTFilterSet
    filterset_form = forms.ONTFilterForm

class ONTEditView(ObjectEditView, View):
    alt_title = "ONT"
    queryset = ONT.objects.all()
    model_form = forms.ONTForm

class GPONSplitterListView(ObjectListView, View):
    alt_title = "GPON Splitters"
    queryset = GPONSplitter.objects.all()
    table = tables.GPONSplitterTable
    filterset = filters.GPONSplitterFilterSet
    filterset_form = forms.GPONSplitterFilterForm

class GPONSplitterEditView(ObjectEditView, View):
    alt_title = "GPON Splitter"
    queryset = GPONSplitter.objects.all()
    model_form = forms.GPONSplitterForm


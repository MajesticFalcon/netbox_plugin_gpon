from django.urls import path
from django.http import HttpResponse

from netbox_plugin_gpon.views import *
from .netbox_plugin_gpon.views import generic

urlpatterns = [

    path("olts/", OLTListView.as_view(), name="olt_list"),
    path("olt/add", OLTEditView.as_view(), name="olt_add"),
    path("olt/<int:pk>", OLTView.as_view(), name="olt"),

    path("gponsplitters/", GPONSplitterListView.as_view(), name="gponsplitter_list")
]
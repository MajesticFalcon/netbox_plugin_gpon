from django.urls import path
from django.http import HttpResponse

from netbox_plugin_gpon.views import *
from .netbox_plugin_gpon.views import generic

urlpatterns = [

    path("", HomeView.as_view(), name='home'),

    path("olts/", OLTListView.as_view(), name="olt_list"),
    path("olt/add", OLTEditView.as_view(), name="olt_add"),
    path("olt/edit/<int:pk>", OLTEditView.as_view(), name="olt_edit"),
    path("olt/<int:pk>", OLTView.as_view(), name="olt"),

    path("onts", ONTListView.as_view(), name="ont_list"),
    path("ont/add", ONTEditView.as_view(), name="ont_add"),
    path("ont/<int:pk>", ONTEditView.as_view(), name="ont_edit"),

    path("gponsplitter/<int:pk>", GPONSplitterEditView.as_view(), name="gponsplitter_edit"),
    path("gponsplitters/", GPONSplitterListView.as_view(), name="gponsplitter_list"),
    path("gponsplitter/add", GPONSplitterEditView.as_view(), name="gponsplitter_add")

]
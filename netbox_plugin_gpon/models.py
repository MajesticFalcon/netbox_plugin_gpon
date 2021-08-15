from django.db import models
from netbox.models import ChangeLoggedModel
from datetime import datetime
from django.urls import reverse
from dcim.models import Manufacturer, DeviceType, Interface, Device, Site
from django.contrib.auth.models import User
from ipam.fields import IPAddressField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

   
class ISPDevice(ChangeLoggedModel):
    name = models.CharField(max_length=255)
    comments = models.TextField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    device_type = models.ForeignKey(DeviceType, on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)

class ISPActiveDevice(ISPDevice):
    ip_address = IPAddressField(blank=True, null=True, default="", verbose_name="IP Address")
    type = models.CharField(max_length=255, null=True, blank=True)


class OLT(ISPActiveDevice):
    def get_absolute_url(self):
        return reverse("plugins:netbox_plugin_gpon:olt", args=[self.pk])
    pass

class GPONSplitter(ISPDevice):

    UPLINK_TYPE_CHOICES = (
        ("CASCADED", "CASCADED"),
        ("DIRECT", "DIRECT")
    )

    limit = models.Q(model = 'olt') | models.Q(model = 'gponsplitter')

    uplink_type = models.CharField(max_length=255, choices=UPLINK_TYPE_CHOICES, verbose_name="Uplink connection type")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Uplink object type", limit_choices_to=limit)
    object_id = models.PositiveIntegerField(verbose_name="Uplink id")
    uplink_port = GenericForeignKey('content_type', 'object_id')

    def get_absolute_url(self):
        return reverse("plugins:netbox_plugin_gpon:gponsplitter_edit", args=[self.pk])

    def __str__(self):
        return self.name

    def parent(self):
        if self.content_type.model == 'olt':
            return 1 #OLT.objects.get(pk=self.object_id).name
        else:
            return GPONSplitter.objects.get(pk=self.object_id).name

class ONT(ISPActiveDevice):
    uplink = models.ForeignKey(GPONSplitter, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("plugins:netbox_plugin_gpon:ont_edit", args=[self.pk])

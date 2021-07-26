from django.contrib import admin
from .models import *

@admin.register(OLT)
class OLTAdmin(admin.ModelAdmin):
    exclude = ('',)

@admin.register(GPONSplitter)
class GPONSplitterAdmin(admin.ModelAdmin):
    exclude = ('',)


@admin.register(ONT)
class ONTAdmin(admin.ModelAdmin):
    exclude = ('',)
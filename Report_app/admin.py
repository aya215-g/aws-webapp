import imp
from django.contrib import admin

from RequestApp.models import RequestData
from search.models import Patient
from .models import Report, Specimen, Docter_Report

# Register your models here.
admin.site.register((Report, Specimen,Patient,RequestData,Docter_Report))

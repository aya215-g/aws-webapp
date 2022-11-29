from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from django.apps import apps

from search.models import Patient
from .models import Report, Specimen
from search.models import Patient
# Create your views here.
@login_required
def addNewReport (request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        nature_of_specimen = request.POST['nature_of_specimen']
        age = request.POST['age']
        gender = request.POST['gender']
        report_issued_at = request.POST['report_issued_at']
#        pathology_number = request.POST['pathology_number']
        groos_examination = request.POST['groos_examination']
        microscopic_examination = request.POST['microscopic_examination']
        diagnosis = request.POST['diagnosis']
        signature = request.POST['signature']

        p=Patient(patient_name=patient_name,patient_age=age,patient_gender=gender)
        p.save()
        spec=Specimen(nature_of_specimen=nature_of_specimen)
        spec.save()
        report = Report( patient=p, specimen=spec,
         report_issued_at = report_issued_at, groos_examination = groos_examination,
        microscopic_examination=microscopic_examination, diagnosis= diagnosis, signature= signature)

        report.save()
        return redirect('/AddNewReport',report)

    else:
        return render(request, 'Report_app/NewReport.html')

@login_required
def addNewSpecimen(request):
    if request.method == 'POST':
        nature_of_specimen = request.POST['nature_of_specimen']
        specimen_size = request.POST['specimen_size']
        number_of_slides = request.POST['number_of_slides']
        specimen = Specimen(nature_of_specimen=nature_of_specimen, specimen_size=specimen_size, number_of_slides=number_of_slides)
        specimen.save()

        return redirect('/AddNewSpecimen')

    else:
        return render(request, 'Report_app/SpecimenData.html')



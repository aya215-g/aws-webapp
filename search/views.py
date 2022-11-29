from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.apps import apps


from Report_app.forms import ReportForm, ReportForm1
from Report_app.models import Specimen
from .models import Patient

Request = apps.get_model('RequestApp', 'RequestData')
Report = apps.get_model('Report_app', 'Report')


# Create your views here.
@login_required
def searchReports(request):
    if request.method == 'POST':
        fetch_report = request.POST['search']
        fetched_report = Report.objects.filter(patient_name=fetch_report)
        return render(request, 'search/searchreports.html', {'show_report': fetched_report})

    fetched_report = Report.objects.all()
    return render(request, 'search/searchreports.html', {'show_report': fetched_report})


def showReport(request, rep_id):
    fetched_report = Report.objects.get(pk=rep_id)
    fetched_patient = fetched_report.patient
    spec = fetched_report.specimen
    return render(request, 'search/show_report.html',{'report': fetched_report,'patient': fetched_patient, 'spec': spec})

def updatereport(request, rep_id):
    fetched_report=Report.objects.get(pk=rep_id)
    fetched_patient=fetched_report.patient
    context = {}

#    fetched_report = get_object_or_404(report, pk=rep_id)
    # pass the object as instance in form
    form = ReportForm1(request.POST or None, instance=fetched_report)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('/searchReports')
    # add form dictionary to context
    context["form"] = form

    return render(request,'Report_app/update_report1.html', context)

def update_report(request, rep_id):
    fetched_report = Report.objects.get(pk=rep_id)
    fetched_patient = fetched_report.patient
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        patient_age = request.POST['age']
        patient_gender = request.POST['gender']
        report_issued_at = request.POST['report_issued_at']
        groos_examination = request.POST['groos_examination']
        microscopic_examination = request.POST['microscopic_examination']
        diagnosis = request.POST['diagnosis']
        signature = request.POST['signature']

        fetched_patient.patient_name=patient_name
        fetched_patient.patient_age=patient_age
        fetched_patient.patient_gender=patient_gender
        fetched_patient.save()

        fetched_report.patient=fetched_patient
        fetched_report.report_issued_at = report_issued_at
        fetched_report.groos_examination = groos_examination
        fetched_report.microscopic_examination = microscopic_examination
        fetched_report.diagnosis = diagnosis
        fetched_report.signature = signature

        fetched_report.save()
        fetched_patient.refresh_from_db()
        fetched_report.refresh_from_db()
        return redirect('/searchReports')
    #    fetched_report = get_object_or_404(report, pk=rep_id)
    # pass the object as instance in form
    #form = ReportForm(request.POST or None, instance=fetched_report)
    # save the data from the form and
    # redirect to detail_view
   # if form.is_valid():
     #   patient_name = request.POST['patient_name']
    #    patient_age = request.POST['patient_age']
   #     patient_gender = request.POST['patient_gender']
  #      fetched_patient.patient_name=patient_name
 #       fetched_patient.patient_age=patient_age
#        fetched_patient.patient_gender=patient_gender

#        form=form.save()

 #       return redirect('searchReports',form)
    # add form dictionary to context
  #  context={'form':form,'patient': fetched_patient,'report':fetched_report}

    return render(request, 'Report_app/update_report.html', {'form':fetched_report,'patient':fetched_patient})


###########
# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View

from .utils import html_to_pdf
from django.template.loader import render_to_string


# Creating a class based view
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = Report.objects.get(pathology_number=555777)
        open('templates/temp.html', "w").write(render_to_string('search/show_report.html', {'report': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


def openPrintPreview(request, rep_id):
    fetched_report = Report.objects.get(pk=rep_id)
    fetched_patient = fetched_report.patient
    fetched_specimen = fetched_report.specimen

    return render(request, 'search/print_preview.html', {'report': fetched_report,'patient':fetched_patient,'spec':fetched_specimen})


def showSpecimen(request, spec_id):
    fetched_specimen = Specimen.objects.get(pk=spec_id)
    return render(request, 'search/show_specimen.html', {'specimen': fetched_specimen})


def showRequest(request, req_id):
    fetched_request = Request.objects.get(pk=req_id)
    return render(request, 'search/view_request.html', {'request': fetched_request})


def searchRequest(request):
    if request.method == 'POST':
        fetch_request = request.POST['search']
        fetched_request = Request.objects.filter(patient_Nid=fetch_request)
        return render(request, 'search/search_requests.html', {'show_request': fetched_request})

    fetched_request = Request.objects.filter(accepted=False)
    return render(request, 'search/search_requests.html', {'show_request': fetched_request})


def acceptRequest(request, req_id):
    req = Request.objects.get(pk=req_id)
    if request.method == 'POST':
        patient_type = request.POST['type_p']
        patient_phone = request.POST['phone']

        p = Patient(patient_name=req.patient_name,
                    patient_age=req.patient_age,
                    patient_gender=req.patient_sex,
                    patient_NID=req.patient_Nid,
                    patient_type=patient_type,
                    patient_phone=patient_phone
                    )
        p.save()
        req.patient = p
        req.accepted = True
        req.save()
    return render(request, 'search/accepted_request.html')


def showAcceptedRequests(request):
    if request.method == 'POST':
        fetch_request = request.POST['search']
        fetched_request = Request.objects.filter(patient_Nid=fetch_request, accepted=True, report_created=False)
        return render(request, 'search/accepted_request.html', {'show_request': fetched_request})

    fetched_request = Request.objects.filter(accepted=True, report_created=False)
    return render(request, 'search/accepted_request.html', {'show_request': fetched_request})


@login_required
def addNewReportToRequest(request, pat_id):
    patient = Patient.objects.get(patient_NID=pat_id)
    req = Request.objects.get(patient=patient)

    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        patient_age = request.POST['age']
        patient_gender = request.POST['gender']
        number_of_slides=request.POST['number_of_slides']
        nature_of_specimen = request.POST['nature_of_specimen']
        report_issued_at = request.POST['report_issued_at']
        groos_examination = request.POST['groos_examination']
        microscopic_examination = request.POST['microscopic_examination']
        diagnosis = request.POST['diagnosis']
        signature = request.POST['signature']

        req.report_created = True
        req.save()

        patient.patient_name = patient_name
        patient.patient_age = patient_age
        patient.patient_gender = patient_gender
        patient.save()
        spec = Specimen(nature_of_specimen=nature_of_specimen,number_of_slides=number_of_slides)
        spec.save()

        report = Report(patient=patient, specimen=spec,

                        report_issued_at=report_issued_at, groos_examination=groos_examination,
                        microscopic_examination=microscopic_examination, diagnosis=diagnosis, signature=signature)
        report.save()
        return redirect('/searchReports',report)

    else:
        return render(request, 'search/addreport_torequest.html', {'patient': patient})


def editSpecimen(request, spec_id):
    spec = Specimen.objects.get(pk=spec_id)
    if request.method == 'POST':
        nature_of_specimen = request.POST['nature_of_specimen']
        specimen_size = request.POST['specimen_size']
        number_of_slides = request.POST['number_of_slides']
        spec.nature_of_specimen = nature_of_specimen
        spec.specimen_size = specimen_size
        spec.number_of_slides = number_of_slides
        spec.save()
        spec.refresh_from_db()
        return redirect('/searchReports')

    return render(request, 'search/speciman_edit.html', {'spec': spec})

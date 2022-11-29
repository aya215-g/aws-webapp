from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import apps

report=apps.get_model('Report_app','Report')

#Create your views here.
@login_required
def home(request):
    if request.method=='POST':
        fetch_report=request.POST['search']
        fetched_report=report.objects.filter(patient_name=fetch_report)
        return render(request,'search/searchreports.html',{'show_report':fetched_report})

    return render(request,'home.html')
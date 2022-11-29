"""pathprog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path 
from .views import newrequest
from Report_app.views import addNewReport, addNewSpecimen
from RequestApp.views import openContact
from search.views import searchReports, showReport, update_report, GeneratePdf, openPrintPreview, showSpecimen, \
    showRequest, searchRequest, acceptRequest, showAcceptedRequests, addNewReportToRequest, editSpecimen, \
    updatereport

urlpatterns = [

    path('NewRequest', newrequest,name='NewRequest'),
    path('AddNewReport', addNewReport,name='AddNewReport'),
    path('AddNewSpecimen', addNewSpecimen, name='add_new_specimen'),
    path('contact_us',openContact,name='contact_us'),
    path('searchReports',searchReports,name='searchReports'),
    path('showReport <int:rep_id>',showReport,name='showReport'),
    path('update_report <int:rep_id>', update_report, name='update_report'),
    path('pdf/', GeneratePdf.as_view(), name='pdf'),
    path('openPrintPreview <int:rep_id>', openPrintPreview, name='openPrintPreview'),
    path('showSpecimen/<int:spec_id>', showSpecimen, name='showSpecimen'),
    path('showRequest <int:req_id> ', showRequest, name='showRequest'),
    path('searchRequest', searchRequest, name='searchRequest'),
    path('acceptRequest <int:req_id>', acceptRequest, name='acceptRequest'),
    path('showAcceptedRequests', showAcceptedRequests, name='showAcceptedRequests'),
    path('editSpecimen <int:spec_id>', editSpecimen, name='editSpecimen'),
    path('addNewReportToRequest <int:pat_id>', addNewReportToRequest, name='addNewReportToRequest'),
    path('updatereport <int:rep_id>', updatereport, name='updatereport'),
]

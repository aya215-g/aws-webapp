from django.shortcuts import render

from search.models import Patient
from .models import RequestData
from django.contrib.auth.decorators import login_required

@login_required
def newrequest(request):
    if request.method == 'POST':

        patient_name= request.POST.get("name_patient", False)
        patient_Nid= request.POST.get("national_id" , False)
        patient_sex=  request.POST.get("sex_patient", False)
        patient_age=  request.POST.get("age_patient", False)

        referring_physician_name= request.POST.get("name_ph", False)
        referring_physician_deprt= request.POST.get("reffering_d", False)
        referring_physician_phone= request.POST.get("phone_ph", False)

        Clinical_History_And_Investigation= request.POST.get("c_history", False)
        Previous_pathology_report= request.POST.get("p_history", False)
        Nature_of_the_specimen= request.POST.get("nature_spec", False)

        new_request = RequestData(
            patient_name=patient_name, patient_Nid=patient_Nid,
            patient_sex=patient_sex, patient_age=patient_age,
            referring_physician_name=referring_physician_name,
            referring_physician_deprt=referring_physician_deprt,
            referring_physician_phone=referring_physician_phone,
            Clinical_History_And_Investigation=Clinical_History_And_Investigation,
            Previous_pathology_report=Previous_pathology_report, Nature_of_the_specimen=Nature_of_the_specimen)
        new_request.save()

    return render (request, 'RequestApp/NewRequest.html', {})



# open contact_us page

def openContact(request):
    return render(request,'contact.html')

#def latest_reqs(request):
 #   if request.method == 'POST':
  #      latQ = request.POST['search']
   #     latestQ = RequestData.objects.filter(patient_name=latQ)
    #    return render(request, 'search/searchreports.html', {'show_report': latestQ})

 #   latestQ = RequestData.objects.all()
  #  return render(request, 'RequestApp/latest_req.html', {'latest_req':latestQ})

#def latest_request(request,req_id):
   # latestQ = RequestData.objects.get(pk=req_id)
    #return render(request,'RequestApp/request.html',{'latest_req':latestQ})

#def prev_req(request):
 #   preQ=RequestData.objects.all()
  #  return render(request, 'RequestApp/prev_req.html', {'previous_req':preQ})


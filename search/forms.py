from django import forms
from .models import Patient

class acceptPatient(forms.ModelForm):
    class Meta:
        model=Patient
        exclude=['patient_name','patient_age','patient_gender','patient_NID']



'''

def acceptRequest(request,req_id):
    req=Request.objects.get(pk=req_id)
    form_1 =acceptPatient(request.POST or None,request.FILES or None)
    if form_1.is_valid():
        form_1=form_1.save(commit=False)
        form_1.patient_name=req.patient_name
        form_1.patient_age=req.patient_age
        form_1.patient_gender=req.patient_sex
        form_1.patient_NID=req.patient_Nid
        form_1.save()
        return redirect('searchRequest')

    return render(request,"search/.html",{'department':dept,'form_1':form_1})


'''
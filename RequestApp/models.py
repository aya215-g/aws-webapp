#from wsgiref.handlers import format_date_time
from django.db import models

# Create your models here.
from search.models import Patient


class RequestData(models.Model):
    rq_date=models.DateField(auto_now_add=True,auto_created = True,blank=True)
#    rq_specimen_no=models.IntegerField()

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    patient_name= models.CharField(max_length=50,default='patient_name')
    patient_Nid=models.CharField(max_length=14,default='12348615')
    patient_sex=models.CharField(max_length=10,choices=gender_choices,default='Male')
    patient_age=models.PositiveIntegerField(default='21')
    patient=models.ForeignKey(Patient, related_name='patient_has_a_request', on_delete=models.CASCADE,null=True,blank=True)

    referring_physician_name=models.CharField(max_length=60)
    referring_physician_deprt=models.CharField(max_length=60)
    referring_physician_phone=models.BigIntegerField()

    Clinical_History_And_Investigation=models.TextField()

    Previous_pathology_report=models.TextField()

    Nature_of_the_specimen=models.TextField()
    accepted=models.BooleanField(default=False)
    report_created=models.BooleanField(default=False)

    def __str__(self) :
        return self.patient_name


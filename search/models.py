from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_name=models.CharField(max_length=50,default=False)
    patient_age=models.IntegerField(default=False)
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    patient_gender = models.CharField(max_length=6, choices=gender_choices,default='Male')
    type_choices = (
        ('OS', 'OS'),
        ('S', 'S'),
        ('R', 'R'),
        ('M', 'M'),
    )
    patient_type=models.CharField(max_length=10,choices=type_choices,default='OS')
    patient_phone=models.CharField(max_length=20,null=True,blank=True,default=False)
    patient_NID=models.CharField(max_length=20,default='1234568')

    def __str__(self) :
        return self.patient_name
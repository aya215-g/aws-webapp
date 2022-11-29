from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from search.models import Patient
from django.utils import timezone
class Specimen(models.Model):
    nature_of_specimen = models.CharField(max_length=50)
    size_choice = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    specimen_size = models.CharField(max_length=6, choices=size_choice,null=True,blank=True)
    number_of_slides = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nature_of_specimen

class Report(models.Model):
    patient = models.ForeignKey(Patient, related_name='patient_has_a_report', on_delete=models.CASCADE, null=True,
                                blank=True)
    specimen = models.OneToOneField(Specimen, related_name='specimen_belongs_to_report', on_delete=models.CASCADE,
                                    null=True, blank=True)

   
    report_issued_at = models.DateField(default=timezone.now().year)
    pathology_number = models.AutoField(primary_key=True, auto_created=True)

    groos_examination = models.TextField(blank=True)
    microscopic_examination = models.TextField(blank=True)
    diagnosis = models.TextField(blank=True)
    signature = models.CharField(max_length=50,blank=True)
    user = models.ManyToManyField(User, through='Docter_Report', blank=True)
    def __str__(self):
        return str(self.pathology_number)

class Docter_Report(models.Model):
    doc=models.ForeignKey(User,on_delete=models.CASCADE)
    rep=models.ForeignKey(Report,on_delete=models.CASCADE)
    def __str__(self):
        return self.doc



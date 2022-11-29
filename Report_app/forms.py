from django import forms

from search.models import Patient
from .models import Report

# creating a form
class ReportForm1(forms.ModelForm):
	# create meta class
	class Meta:
		# specify model to be used
		model = Report
		# specify fields to be used
		exclude = ['user']

# creating a form
class ReportForm(forms.ModelForm):
#	def __init__(self, *args, **kwargs):
#		super(ReportForm, self).__init__(*args, **kwargs)
		# Making name required
#		self.fields['patient_name'].required = True
#		self.fields['patient_age'].required = True
#		self.fields['patient_gender'].required = True
	patient_name = forms.CharField(max_length=50)
	patient_age = forms.IntegerField()
	gender_choices = (
	    ('Male', 'Male'),
	   ('Female', 'Female'),
	 )
	patient_gender = forms.ChoiceField( choices=gender_choices)
	# create meta class
	class Meta:
		# specify model to be used
		model = Report
		# specify fields to be used
		include= ['patient_name','patient_age','patient_gender',]
		exclude = ['user']

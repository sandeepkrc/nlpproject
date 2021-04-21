from django import forms 

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class Contactus(forms.Form):
    email_address=forms.EmailField()
    name = forms.CharField(max_length=15)
    number=forms.CharField()
    message=forms.CharField()
class Intern(forms.Form):
    name = forms.CharField(max_length=15)
    email_address=forms.EmailField()
    number=forms.CharField()
    cover_letter = forms.CharField()
    upload_resume = forms.FileField()
class Consultform(forms.Form):
    first_name = forms.CharField(max_length=20)
    country = CountryField(blank_label='(select country code)').formfield(widget=CountrySelectWidget(attrs={
		'class':'custom-select d-block w-100',
		'zip':'id'
		}))
    # arer_code = forms.ChoiceField(, choices=[CHOICES])
    phone_no = forms.CharField(max_length=10)
    email = forms.EmailField()
    detaits_of_consultions  = forms.CharField(max_length=200)
    appointment = forms.TimeField() 

class Payments(forms.Form):
    pass
    

    

    


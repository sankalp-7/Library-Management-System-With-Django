from django import forms
from . import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class IssuedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn=forms.ModelChoiceField(queryset=models.book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    enrollment=forms.ModelChoiceField(queryset=models.student.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.student
        fields=['enrollment']


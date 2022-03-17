from django import forms
from django.forms import ModelForm

from .models import ApplicationModel

class ApplicationForm(ModelForm):
    class Meta:
        model=ApplicationModel
        fields = "__all__"
        exclude=('user','job','jobid','status')
        widgets={

            "name":forms.TextInput(attrs={"class": "form-control"}),
            "phone":forms.TextInput(attrs={"class": "form-control"}),
            "location":forms.TextInput(attrs={"class": "form-control"}),
            "qualification":forms.TextInput(attrs={"class": "form-control"}),
            "experience":forms.NumberInput(attrs={"class": "form-control"}),
            "resume":forms.FileInput(attrs={"class":"form-control"})

        }
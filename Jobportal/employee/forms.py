from django import forms
from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.forms import UserCreationForm
from .models import MyUser,Jobs
from candidate.models import ApplicationModel


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=MyUser
        fields=["name","email","date_of_birth","phone","role","password1","password2"]
        widgets={
            "name":forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control","type":"date"}),
            "phone":forms.TextInput(attrs={"class": "form-control"}),
            "role":forms.Select(attrs={"class": "form-select"}),


        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class JobPostingForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields=["designation","description","company","location","skills","salary"]
        exclude=('user',)
        widgets={
            "designation":forms.TextInput(attrs={"class": "form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "company":forms.TextInput(attrs={"class": "form-control"}),
            "location":forms.TextInput(attrs={"class": "form-control"}),
            "skills":forms.Select (attrs={"class": "form-select"}),
            "salary":forms.NumberInput(attrs={"class": "form-control"}),


        }

class ApplicationProcessForm(forms.ModelForm):
    class Meta:
        model=ApplicationModel
        fields =["status"]
        widgets={
            "status":forms.Select(attrs={"class":"form-select"})
        }
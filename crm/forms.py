from django import forms
from crm.models import *
from django.contrib.auth.models import User



class EmployeeModelForms(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"
        
    widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.TextInput(attrs={"class":"form-control"}),
            "contact":forms.TextInput(attrs={"class":"form-control","rows":5}),
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"})
            
        }
    


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-conrol"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-conrol"}))    
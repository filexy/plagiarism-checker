from django import forms
from .models import *

class UploadFileForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Title",                
                "class": "form-control form-control-alternative",
               
            }
        ))
    authors = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Authors",                
                "class": "form-control form-control-alternative",
              
                
            }
        ))
    year = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Year Submitted",                
                "class": "form-control form-control-alternative",
           
            }
        ))
    
    type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Project Type",                
                "class": "form-control form-control-alternative",
            }
        ))
    class Meta:
        model = Uploads
        fields = ('title','authors','year','type','file')
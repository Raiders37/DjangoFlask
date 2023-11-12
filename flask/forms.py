from django import forms
from .models import Data, Hepatite_data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'experience', 'test_score', 'interview_score']


class HepatiteForm(forms.ModelForm):
    class Meta:
        model = Hepatite_data
        fields = ['name', 'age', 'sex', 'steroide', 
                  'antiviraux', 'fatigue', 'naevi', 
                  'varices', 'ascite', 'bilirubine',
                   'phostate', 'sgot', 'albumin',
                     'protime', 'histology']
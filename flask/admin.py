from django.contrib import admin

# Register your models here.
from .models import Data, Hepatite_data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'test_score', 'interview_score', 'predictions')


admin.site.register(Data, DataAdmin)

class HepatiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex', 'steroide', 
                  'antiviraux', 'fatigue', 'naevi', 
                  'varices', 'ascite', 'bilirubine',
                   'phostate', 'sgot', 'albumin',
                     'protime', 'histology', 'predictions')


admin.site.register(Hepatite_data, HepatiteAdmin)
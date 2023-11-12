from django.shortcuts import render, redirect
from .forms import DataForm, HepatiteForm
from .models import Data, Hepatite_data
import pandas as pd
import calendar
from calendar import HTMLCalendar
from datetime import datetime
import csv
from django_tables2.tables import Table

# Create your views here.


def index(request, year = datetime.now().year, month = datetime.now().strftime('%B'), day = datetime.now().strftime('%d')):
    
    month = month.title()
    #convert month from namr to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    day = day.title()


    #create calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )

    # car for time
    now = datetime.now()

    #get curent time
    time = now.strftime('%I:%M:%S %P')

    #Get current year
    current_year = now.year

    return render(request, 
        'flask/index.html', {
        'day' : day,
        'year': year,
        'month': month,
        'month_number' : month_number,
        'cal' : cal,
        'current_year' : current_year,
        'now' : now,
        'time' : time,
        })


#############################################################

def salaire(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'flask/salaire.html', context)

##############################################################

def predictions(request):
    predicted_sports = Data.objects.all()
    context = {
        'predicted_sports': predicted_sports
    }
    return render(request, 'flask/predictions.html', context)

###############################################################

def hepatite(request):
    if request.method == 'POST':
        form = HepatiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hepatite-prediction')
    else:
        form = HepatiteForm()
    context = {
        'form': form,
    }
    
    return render(request, 'flask/hepatite.html', context)

################################################################

def hepatite_prediction(request):
    predicted_hepatite = Hepatite_data.objects.all()
    context = {
        'predicted_hepatite': predicted_hepatite
    }
    
    return render(request, 'flask/hepatite_prediction.html', context)

###################################################################

def hepatite_dataset(request):

    df = pd.read_csv("data/clean_dataset.csv")
    context = {"df" : df}
	#return render("dataset.html",df_table=df)
    return render(request, 'flask/hepatite_dataset.html', context)

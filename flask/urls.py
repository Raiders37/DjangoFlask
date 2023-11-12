from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='dashboard-index'),
    path('salaire/', views.salaire, name='salaire-index'),
    path('predictions/', views.predictions, name='dashboard-predictions'),
    path('hepatite/', views.hepatite, name='hepatite-index'),
    path('hepatite_prediction/', views.hepatite_prediction, name='hepatite-prediction'),
    path('hepatite_dataset/', views.hepatite_dataset, name='hepatite-dataset'),

]
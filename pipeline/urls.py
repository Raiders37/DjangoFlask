from django.urls import path
from . import views

urlpatterns = [

   
    path('pipeline/', views.pipeline_index, name='pipeline-index'),
    

]
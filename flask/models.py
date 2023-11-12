from django.db import models

# Create your models here.

import numpy as np
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import pickle

# Create your models here.

GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)

YES_NO = (
    (0, 'Oui'),
    (1, 'Non'),
)

######################################################################################

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    experience = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], null=True)
    test_score = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], null=True)
    interview_score = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], null=True)
    predictions = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = pickle.load(open('flask/model_pkl/model.pkl', 'rb'))
        self.predictions = ml_model.predict(
            [[self.experience, self.test_score, self.interview_score]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
    
######################################################################################

class Hepatite_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)], default=10)
    sex = models.PositiveIntegerField(choices=GENDER, default=0)
    steroide = models.PositiveIntegerField(choices=YES_NO, default=0)
    antiviraux = models.PositiveIntegerField(choices=YES_NO, default=0)
    fatigue = models.PositiveIntegerField(choices=YES_NO, default=0)
    naevi = models.PositiveIntegerField(choices=YES_NO, default=0)
    varices = models.PositiveIntegerField(choices=YES_NO, default=0)
    ascite = models.PositiveIntegerField(choices=YES_NO, default=0)
    bilirubine = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], default=0)
    phostate = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], default=0)
    sgot = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], default=0)
    albumin = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], default=0)
    protime = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(19)], default=0)
    histology = models.PositiveIntegerField(choices=YES_NO, default=0)
    
    predictions = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load(open('flask/model_pkl/logistic_regression_model.pkl', 'rb'))
        self.predictions = ml_model.predict(
            [[self.age, self.sex, self.steroide,
              self.antiviraux, self.fatigue, self.naevi,
              self.varices, self.ascite, self.bilirubine,
              self. phostate, self.sgot, self.albumin,
              self.protime, self.histology]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
# -*- coding: utf-8 -*-
from django import forms

from .models import Patient, Visit

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'pesel')

class VisitForm(forms.ModelForm):

    class Meta:
        model = Visit
        fields = ('description',)
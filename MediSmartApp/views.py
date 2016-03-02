# -*- coding: utf-8 -*-

import sys
import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from .forms import PatientForm, VisitForm
from .models import Patient, Visit


def patients_gen():
    patients = Patient.objects.all().order_by('last_name')
    for p in patients:
        yield unicode(p).encode('utf-8') + '\n'

def visits_gen():
    visits = Visit.objects.all().order_by('visit_date')
    for v in visits:
        yield unicode(v).encode('utf-8') +'\n'


def backup_patients():
    run_backup(patients_gen, 'PACJENTÓW')

def backup_visits():
    run_backup(visits_gen, 'WIZYT')


def run_backup(gen, f):
    today = datetime.datetime.now()
    patients = Patient.objects.all()
    if 'linux' in sys.platform:
        backup_file = '/tmp/BACKUP_{0}.txt'.format(f)
    elif 'win32' in sys.platform:
        backup_file = 'C:\\users\\hania\\Desktop\\BACKUP_{0}.txt'.format(f)
    else:
        return
    with open(backup_file, 'w+') as f:
        f.write('Database saved on {0}\n'.format(today))
        # for p in patients:
        #     f.write(unicode(p).encode('utf-8'))
        #     f.write('\n')
        f.writelines(gen())


def home(request):
    template = loader.get_template('MediSmartApp/home.html')
    return HttpResponse(template.render())


def patient_index(request):
    patients = Patient.objects.all().order_by('last_name')
    template = loader.get_template('MediSmartApp/patient_index.html')
    context = RequestContext(request, {
        'patients': patients,
    })
    return HttpResponse(template.render(context))

def visit_index(request):
    visits = Visit.objects.all().order_by('visit_date')
    template = loader.get_template('MediSmartApp/visit_index.html')
    context = RequestContext(request, {
        'visits': visits,
    })
    return HttpResponse(template.render(context))

def patient_details(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    visits = Visit.objects.filter(patient=patient)
    template = loader.get_template('MediSmartApp/patient_details.html')
    context = RequestContext(request, {
        'patient': patient,
        'visits': visits,
    })
    return HttpResponse(template.render(context))

def visit_details(request, visit_id):
    visit = Visit.objects.get(pk=visit_id)
    patient = visit.patient
    template = loader.get_template('MediSmartApp/visit_details.html')
    context = RequestContext(request, {
        'visit': visit,
        'patient': patient,
    })
    return HttpResponse(template.render(context))

def patient_edit(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            backup_patients()
            #return redirect('/MediSmartApp/patient_details/' + patient_id)
            return redirect('/MediSmartApp/patient_details/'+ patient_id)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'MediSmartApp/patient_edit.html', {'form': form, 'patient_id': patient_id})

    #return HttpResponse("You're editing patient %s." % patient_id)

def visit_edit(request, patient_id, visit_id):
    visit = Visit.objects.get(pk=visit_id)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            backup_visits()
            return redirect('/MediSmartApp/patient_details/' + patient_id)
    else:
        form = VisitForm(instance=visit)
    return render(request, 'MediSmartApp/visit_edit.html', {'form': form, 'patient_id': patient_id})

def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            backup_patients()
            return redirect('patient_index')
    else:
        form = PatientForm()
    return render(request, 'MediSmartApp/patient_add.html', {'form': form})

def visit_add(request, patient_id):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.patient = Patient.objects.get(pk=patient_id)
            visit.visit_date = datetime.datetime.now()
            visit.save()
            backup_visits()
            return redirect('/MediSmartApp/patient_details/' + patient_id)
    else:
        form = VisitForm()
    return render(request, 'MediSmartApp/visit_add.html', {'form': form, 'patient_id': patient_id})

def patient_delete(request, patient_id):
    Patient.objects.filter(pk=patient_id).delete()

    patients = Patient.objects.all()
    context = RequestContext(request, {
        'patients': patients,
    })
    template = loader.get_template('MediSmartApp/patient_index.html')
    backup_patients()
    return HttpResponse(template.render(context))

def visit_delete(request, visit_id, patient_id):
    Visit.objects.filter(pk=visit_id).delete()

    loader.get_template('MediSmartApp/patient_details.html')
    backup_visits()
    return redirect('/MediSmartApp/patient_details/' + patient_id)
    #return HttpResponse(template.render(context))


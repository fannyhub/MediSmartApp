from django.test import TestCase
from django.http import HttpRequest
from views import patient_add, patient_delete
from models import Patient



class MyTests(TestCase):

    def setUp(self):
        self.request = HttpRequest

    def test_adding(self):
        added_patient = patient_add(self.request)
        print added_patient.first_name
        new_patient = Patient.objects.get(first_name = added_patient.first_name)

    def test_deleting(self):
         #patients = (a, b, c)
        #[for p in patients Patient(self.request, a, b, c) for a, b, c in p]
        #patient_add(self.request, 'A', 'B', 1)
        #patient_add(self.request, 'Aa', 'Bb', 11)
        #patient_add(self.request, 'Aaa', 'Bbb', 111)
        print Patient.objects.all()
        patient_delete(self.request, 2)
        print Patient.objects.all()
        #self.assertRaises(DoesNotExist, lambda: Patient.objects.get(id=2))



# -*- coding: utf-8 -*-
from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pesel = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        # return '{0} {1} {2}'.format(self.last_name, self.first_name, self.pesel)
        return self.last_name + " " + self.first_name + " " + str(self.pesel)


class Visit(models.Model):
    visit_date = models.DateTimeField('date of the visit')
    patient = models.ForeignKey(Patient)
    description = models.TextField()

    def __unicode__(self):
        return str(self.visit_date) + ' ' + self.description 



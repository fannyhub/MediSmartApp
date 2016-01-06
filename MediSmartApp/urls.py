from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home page'),
    url(r'^patient_index/', views.patient_index, name='patient_index'),
    url(r'^visit_index/', views.visit_index, name='visit_index'),
    url(r'^patient_details/(?P<patient_id>[0-9]+)/$', views.patient_details, name='patient_details'),
    url(r'^visit_details/(?P<visit_id>[0-9]+)/$', views.visit_details, name='visit_details'),
    url(r'^patient_edit/(?P<patient_id>[0-9]+)/$', views.patient_edit, name='patient_edit'),
    url(r'^(?P<patient_id>[0-9]+)/visit_edit/(?P<visit_id>[0-9]+)/$', views.visit_edit, name='visit_edit'),
    url(r'^patient_add/$', views.patient_add, name='patient_add'),
    url(r'^visit_add/(?P<patient_id>[0-9]+)/$', views.visit_add, name='visit_add'),
    url(r'^patient_delete/(?P<patient_id>[0-9]+)/$', views.patient_delete, name='patient_delete'),
    url(r'^visit_delete/(?P<visit_id>[0-9]+)/(?P<patient_id>[0-9]+)/$', views.visit_delete, name='visit_delete'),
]
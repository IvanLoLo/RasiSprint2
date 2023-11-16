from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.paciente_view, name='paciente_view'),
    path('pacientes/<str:pk>/', views.paciente_view, name='paciente_view'),

    path('medicos/', views.medico_view, name='medico_view'),
    path('medicos/<str:pk>/', views.medico_view, name='medico_view'),
]
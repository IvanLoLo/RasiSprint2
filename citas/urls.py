from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.citas_view, name='citas_view'),
    path('<str:pk>/', views.cita_view, name='cita_view'),
    path('fecha/<str:fecha>/', views.cita_by_fecha_view, name='cita_by_fecha_view'),
    path('mes/<str:mes>/', views.cita_by_mes_view, name='cita_by_mes_view'),
    path('especialidad/<str:especialidad>/', views.cita_by_especialidad_view, name='cita_by_especialidad_view'),
    path('paciente/new', views.paciente_view, name='paciente_view'),
    path('medico/new', views.medico_view, name='medico_view'),
]
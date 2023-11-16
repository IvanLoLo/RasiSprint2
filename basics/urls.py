from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.basics_view, name='basics_view'),
    path('contract/', views.contract_view, name='contract_view'),
]
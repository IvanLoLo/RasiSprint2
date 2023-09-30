import json
from django.shortcuts import render
from django.http import HttpResponse
from .logic import variables_logic as vl
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def citas_view(request):
    print("Primera funcion")
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            cita = vl.get_cita(id)
            cita_dto = serializers.serialize('json', [cita,])
            return HttpResponse(cita_dto, 'application/json')
        else:
            citas = vl.get_citas()
            print("Here", citas)
            citas_dto = serializers.serialize('json', citas)
            return HttpResponse(citas_dto, 'application/json')
        
    if request.method == 'POST':
        cita_dto = vl.create_cita(json.loads(request.body))
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')
        
@csrf_exempt
def paciente_view(request):
    if request.method == 'POST':
        paciente_dto = vl.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
        
@csrf_exempt
def medico_view(request):
    if request.method == 'POST':
        print("Entra", request.body)
        medico_dto = vl.create_doctor(json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        print(medico_dto, medico)
        return HttpResponse(medico, 'application/json')
    
@csrf_exempt
def cita_view(request, pk):
    print("Segunda funcion")
    if request.method == 'GET':
        citas = vl.get_cita(pk)
        citas_dto = serializers.serialize('json', [citas,])
        return HttpResponse(citas_dto, 'application/json')
    
    if request.method == 'PUT':
        cita_dto = vl.update_cita(pk, json.loads(request.body))
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')
    
def cita_by_fecha_view(request, fecha):
    if request.method == 'GET':
        citas = vl.get_citas_by_fecha(fecha)
        citas_dto = json.dumps({"total_citas": citas})
        return HttpResponse(citas_dto, 'application/json')
    
def cita_by_mes_view(request, mes):
    if request.method == 'GET':
        citas = vl.get_citas_by_mes(mes)
        citas_dto = json.dumps({"total_citas": citas})
        return HttpResponse(citas_dto, 'application/json')
    
def cita_by_especialidad_view(request, especialidad):
    if request.method == 'GET':
        citas = vl.get_citas_by_especialidad(especialidad)
        citas_dto = serializers.serialize('json', citas)
        return HttpResponse(citas_dto, 'application/json')
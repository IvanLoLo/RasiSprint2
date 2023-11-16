import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .logic import basics_logic as vl


@csrf_exempt
def basics_view(request):
    if request.method == 'GET':
        return HttpResponse("U get to basics, god job!", 'application/json')

@csrf_exempt
def contract_view(request):
    if request.method == 'POST':
        try:
            # print(request.body)
            contract_dto = vl.create_contract(request.FILES['file'])
            contract = serializers.serialize('json', [contract_dto,])
            return HttpResponse('asd', 'application/json')
        except Exception as e:
            return HttpResponse(e, 'application/json')
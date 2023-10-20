from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def healthCheck(request):
    return HttpResponse('ok')
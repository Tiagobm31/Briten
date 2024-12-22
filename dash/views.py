from django.shortcuts import render

from django.http import JsonResponse
from dash.models import Emprestimos

def get_data(request):
    data = list(Emprestimos.objects.values()) 
    return JsonResponse(data, safe=False)  


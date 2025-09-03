from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "status": "online",
        "message": "Bem-vindo ao Backend Vanguard Tech 🚀",
        "endpoints": ["/api/clientes/"]
    })


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

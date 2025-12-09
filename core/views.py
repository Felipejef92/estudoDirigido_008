from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from .models import Categoria, Unidade, Sala, Status, Bem
from .serializers import (
    CategoriaSerializer,
    UnidadeSerializer,
    SalaSerializer,
    StatusSerializer,
    BemSerializer
)
def home(request):
    return HttpResponse("Bem-vindo ao sistema de inventário de bens!")

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class UnidadeListCreate(generics.ListCreateAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer


class SalaListCreate(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class BemListCreate(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer


class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
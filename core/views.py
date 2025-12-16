from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from drf_spectacular.utils import extend_schema

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



@api_view(["POST"])
@permission_classes([AllowAny])
@extend_schema(
    tags=["Autenticação"],
    summary="Login na API",
    description="Autentica um usuário para uso da API."
)
def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse(
            {"detail": "Credenciais inválidas"},
            status=400
        )

    login(request, user)
    return JsonResponse(
        {"detail": "Login realizado com sucesso"}
    )



@extend_schema(tags=["Categorias"])
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


@extend_schema(tags=["Categorias"])
class CategoriaRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]



@extend_schema(tags=["Unidades"])
class UnidadeListCreate(generics.ListCreateAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


@extend_schema(tags=["Salas"])
class SalaListCreate(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]



@extend_schema(tags=["Status"])
class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


@extend_schema(
    tags=["Bens"],
    summary="Lista e cria bens",
    description="GET liberado. POST exige autenticação."
)
class BemListCreate(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


@extend_schema(tags=["Bens"])
class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
    permission_classes = [IsAuthenticated]
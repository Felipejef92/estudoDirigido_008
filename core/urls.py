from django.urls import path
from .views import (
    api_login,
    CategoriaListCreate,
    UnidadeListCreate,
    SalaListCreate,
    StatusListCreate,
    BemListCreate,
)

urlpatterns = [
    path("categorias/", CategoriaListCreate.as_view()),
    path("unidades/", UnidadeListCreate.as_view()),
    path("salas/", SalaListCreate.as_view()),
    path("status/", StatusListCreate.as_view()),
    path("bens/", BemListCreate.as_view()),
    path("login/", api_login),
]

from django.urls import path
from .views import (
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
]

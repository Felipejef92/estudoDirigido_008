from django.urls import path
from .views import (
    api_login,
    CategoriaListCreateView,
    CategoriaDetailView,
    UnidadeListCreateView,
    UnidadeDetailView,
    SalaListCreateView,
    SalaDetailView,
    StatusListCreateView,
    StatusDetailView,
    BemListCreateView,
    BemDetailView,
)


urlpatterns = [
    path("login/", api_login),

    path("categorias/", CategoriaListCreateView.as_view()),
    path("categorias/<int:pk>/", CategoriaDetailView.as_view()),

    path("unidades/", UnidadeListCreateView.as_view()),
    path("unidades/<int:pk>/", UnidadeDetailView.as_view()),

    path("salas/", SalaListCreateView.as_view()),
    path("salas/<int:pk>/", SalaDetailView.as_view()),

    path("status/", StatusListCreateView.as_view()),
    path("status/<int:pk>/", StatusDetailView.as_view()),

    path("bens/", BemListCreateView.as_view()),
    path("bens/<int:pk>/", BemDetailView.as_view()),
]
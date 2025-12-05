from django.urls import path
from .views import (
    UnidadeListCreate,
    SalaListCreate,
    StatusListCreate,
    BemListCreate,
    BemDetail
)

urlpatterns = [
    path("unidades/", UnidadeListCreate.as_view(), name="unidades"),
    path("salas/", SalaListCreate.as_view(), name="salas"),
    path("status/", StatusListCreate.as_view(), name="status"),
    path("bens/", BemListCreate.as_view(), name="bens"),
    path("bens/<int:pk>/", BemDetail.as_view(), name="bem-detail"),
]

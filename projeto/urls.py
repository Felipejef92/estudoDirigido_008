from django.contrib import admin
from django.urls import path, include
from core.views import home
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),

    # OpenAPI Schema (drf-spectacular)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI (drf-spectacular)
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

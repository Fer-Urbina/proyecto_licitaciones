from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from licitaciones.views import LicitacionViewSet
from tdrs.views import TDRViewSet
from users.views import ProveedorViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Proyecto Licitaciones API",
        default_version='v1',
        description="Documentación para la API",
    ),
    public=True,
    permission_classes=[AllowAny],
)

router = DefaultRouter()
router.register(r'licitaciones', LicitacionViewSet)
router.register(r'tdrs', TDRViewSet)
router.register(r'proveedores', ProveedorViewSet)

urlpatterns = [
    path('api/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/licitaciones/', include('licitaciones.urls')),  # Esto añade las rutas personalizadas
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
]
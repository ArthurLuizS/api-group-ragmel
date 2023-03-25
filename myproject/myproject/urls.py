from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os

schema_view = get_schema_view(
   openapi.Info(
      title="Suporte API",
      default_version='v1',
      description="",
      terms_of_service="",
      contact=openapi.Contact(email="contato@panops.com.br"),
      license=openapi.License(name="BSD License")
   ),
   public=False,
   url=os.environ.get('API_URL', 'http://127.0.0.1:8000'),
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('admin/', admin.site.urls),
   re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/', include('api.urls')),
]

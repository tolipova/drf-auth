from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi

schema_view = swagger_get_schema_view(
    openapi.Info(
        title = 'Post api',
        default_version = '1.0.0',
        description = 'Api documentatsion'
    ),
    public=True
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="schema-swagger-ui"),
]

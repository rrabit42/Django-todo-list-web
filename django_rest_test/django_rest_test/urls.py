from django.conf.urls import url
from django.contrib import admin
from django.db import router
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_url_v1_patterns = [
    # path('v1/', include(), namespace)
]

schema_view = get_schema_view(
    openapi.Info(
        title="API 연습용",
        default_version='v1',
        description="안녕하세요. Open API 문서 페이지도 처음 써보네요.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex'], # flex는 JSON schema를 체크하는 검사기 패키지
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_v1_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-api/', include('rest_framework.urls')),

    # Auto DRF API docs (drf-yasg에서 지원하는 API 문서 자동화 UI(?)들
    # redoc.ui와 swagger.ui를 지원. 이렇게 쓰면 해당 URL로 접속해 원하는 UI를 사용할 수 있음
    url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/v1/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/v1/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]

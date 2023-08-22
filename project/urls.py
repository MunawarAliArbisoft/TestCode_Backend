from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CodeTest API",
        default_version='v1',
        description="The TestCode is an online assessment Center backend project aims to create a robust backend system for managing an online assessment center. Admins can effortlessly create assessments, candidates can register and attempt assessments, and automated code evaluation provides immediate feedback.",
        contact=openapi.Contact(email="mnrkokhar@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path("", include("project.api_urls")),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/candidate/", include("candidate.urls")),
    path("api/assessment/", include("assessment.urls")),
    path("api/question/", include("question.urls")),
    path("api/answer/", include("answer.urls")),
    path("admin/", admin.site.urls),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("api-auth/", include("rest_framework.urls")),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AssessmentViewSet, AssessmentResultViewSet, submit_assessment

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"assessments", AssessmentViewSet, basename="assessment")
router.register(
    r"assessments-result", AssessmentResultViewSet, basename="assessment-result"
)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("submit-assessment/", submit_assessment),
]

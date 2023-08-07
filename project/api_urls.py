from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Define a custom root view that generates a list of URLs
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'candidates': request.build_absolute_uri('/api/candidate/'),
        'assessments': request.build_absolute_uri('/api/assessment/'),
        'questions': request.build_absolute_uri('/api/question/'),
    })

urlpatterns = [
    #  Custom root view
    path('', api_root),
]

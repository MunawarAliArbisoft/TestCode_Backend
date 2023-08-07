from rest_framework import viewsets

from .models import Candidate
from .serializers import CandidateSerializer
from .permissions import CandidatePermission

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [CandidatePermission]

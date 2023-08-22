from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Answer
from .serializers import AnswerSerializer

from candidate.permissions import CandidatePermission


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, CandidatePermission]

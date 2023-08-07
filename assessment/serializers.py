from rest_framework import serializers
from .models import *
from candidate.serializers import CandidateSerializer
from question.serializers import QuestionSerializer

class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = ['id', 'title', 'description', 'date_created', 'date_updated', 'questions']

class AssessmentResultSerializer(serializers.Serializer):
    assessment = AssessmentSerializer()
    candidate = CandidateSerializer()

    class Meta:
        model = AssessmentResult
        fields = ['id', 'assessment', 'candidate', 'score', 'submission_date']

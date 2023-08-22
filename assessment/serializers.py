from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import *
from question.serializers import QuestionSerializer


class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = [
            "id",
            "title",
            "description",
            "date_created",
            "date_updated",
            "questions",
        ]


class AssessmentResultSerializer(serializers.ModelSerializer):
    assessment_id = serializers.ReadOnlyField(source='assessment.id')
    assessment_title = serializers.ReadOnlyField(source='assessment.title')
    candidate_id = serializers.ReadOnlyField(source='candidate.id')
    candidate_email = serializers.ReadOnlyField(source='candidate.email')

    class Meta:
        model = AssessmentResult
        fields = ["id", "score", "submission_date", "assessment_id", "assessment_title", "candidate_id", "candidate_email", "result"]

    def to_internal_value(self, data):
        # Extract candidate email and assessment ID from the incoming data
        candidate_email = data["candidate_id"]
        assessment_id = data["assessment_id"]

        candidate = get_object_or_404(Candidate, email=candidate_email)
        assessment = get_object_or_404(Assessment, id=assessment_id)
       
        return {
            "candidate": candidate,
            "assessment": assessment,
            "score": data.get("score"),
            "result": data.get("result")
        }

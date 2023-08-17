from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import *
from candidate.serializers import CandidateSerializer
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
    assessment = AssessmentSerializer()
    candidate = CandidateSerializer()

    class Meta:
        model = AssessmentResult
        fields = ["id", "score", "submission_date", "assessment", "candidate"]

    def to_internal_value(self, data):
        # Extract candidate email and assessment ID from the incoming data
        candidate_email = data["candidate"]["email"]
        assessment_id = data["assessment"]["id"]

        # Retrieve the Candidate object from the database using the provided email
        try:
            candidate = get_object_or_404(Candidate, email=candidate_email)
        except Candidate.DoesNotExist as e:
            raise serializers.ValidationError("Candidate does not exist.") from e

        # Retrieve the Assessment object from the database using the provided ID
        try:
            assessment = get_object_or_404(Assessment, id=assessment_id)
        except Assessment.DoesNotExist as exc:
            raise serializers.ValidationError("Assessment does not exist.") from exc

        return {
            "candidate": candidate,
            "assessment": assessment,
            "score": data.get("score"),
        }

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

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        candidate_id = self.context["request"].user.id
        assessment_id = validated_data.get("assessment_id")
        question_id = validated_data.get("question_id")
        question_type = validated_data.get("question_type")
        selected_choice_id = validated_data.get("selected_choice_id")
        code = validated_data.get("code")


        defaults = {"question_type":question_type, "selected_choice_id": selected_choice_id, "code": code}

        answer, created = Answer.objects.update_or_create(
            assessment_id=assessment_id,
            candidate_id=candidate_id,
            question_id=question_id,
            defaults=defaults
        )

        return answer

    def to_internal_value(self, data):
        # Get the candidate ID from the request context
        candidate_id = self.context["request"].user.id

        return {
            "candidate_id": candidate_id,
            **data
        }

    def validate(self, data):
        candidate_id = self.context["request"].user.id
        assessment_id = data.get("assessment_id")
        question_id = data.get("question_id")
        question_type = data.get("question_type")
        selected_choice_id = data.get("selected_choice_id")
        code = data.get("code")

        # Check the existence of related objects
        if not Candidate.objects.filter(id=candidate_id).exists():
            raise serializers.ValidationError("Candidate does not exist.")

        if not Assessment.objects.filter(id=assessment_id).exists():
            raise serializers.ValidationError("Assessment does not exist.")

        if not Question.objects.filter(id=question_id, question_type=question_type).exists():
            raise serializers.ValidationError("Question does not exist.")

        if question_type == "MCQ" and not selected_choice_id:
            raise serializers.ValidationError("choice is required for MCQ question.")
        elif question_type == "COD" and not code:
            raise serializers.ValidationError("code is required for COD question.")

        return data

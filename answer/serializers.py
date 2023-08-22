from rest_framework import serializers
from .models import Answer
from question.models import Question
from candidate.models import Candidate
from assessment.models import Assessment

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

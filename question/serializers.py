from rest_framework import serializers

from .models import Question, Choice, TestCase


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'input_data', 'expected_output', 'is_public']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)  # Nested serializer for the related choices
    testcases = TestCaseSerializer(many=True)  # Nested serializer for the related choices

    class Meta:
        model = Question
        fields = ['id', 'assessment', 'text', 'question_type', 'code_template', 'choices', 'testcases']

    def create(self, validated_data):
        testcases = validated_data.pop('testcases')
        choices = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(question=question, **choice)
        for testcase in testcases:
            TestCase.objects.create(question=question, **testcase)
        return question

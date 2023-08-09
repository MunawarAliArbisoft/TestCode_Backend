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
    testcases = TestCaseSerializer(many=True)  # Nested serializer for the related Testcases

    class Meta:
        model = Question
        fields = ['id', 'assessment', 'text', 'question_type', 'code_template', 'choices', 'testcases']

    def create(self, validated_data):
        # Extract the 'testcases' and 'choices' data from the validated data
        testcases = validated_data.pop('testcases')
        choices = validated_data.pop('choices')

        # Create a new Question instance using the remaining validated data
        question = Question.objects.create(**validated_data)

        # Iterate through each choice and associate it with the question
        for choice in choices:
            Choice.objects.get_or_create(question=question, **choice)

        # Iterate through each testcase and associate it with the question
        for testcase in testcases:
            TestCase.objects.get_or_create(question=question, **testcase)

        # Return the newly created question object
        return question

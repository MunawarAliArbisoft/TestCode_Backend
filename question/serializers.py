from rest_framework import serializers
from rest_framework import status

from .models import Question, Choice, TestCase


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "text", "is_correct"]


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ["id", "input_data", "expected_output", "is_public"]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)  # Nested serializer for the related choices
    testcases = TestCaseSerializer(many=True)  # Nested serializer for the related Testcases

    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "question_type",
            "code_template",
            "choices",
            "testcases",
        ]

    def validate(self, data):
        question_type = data.get("question_type")
        choices = data.get("choices")
        testcases = data.get("testcases")

        if question_type == "MCQ" and len(choices) < 2:
            raise serializers.ValidationError(
                {"message": "MCQs must have at least 2 choices.",
                 "status":str(status.HTTP_400_BAD_REQUEST)}
            )
        elif question_type == "COD" and len(testcases) < 1:
            raise serializers.ValidationError(
                {"message": "Coding questions must have at least 1 test case.",
                "status":str(status.HTTP_400_BAD_REQUEST)}
            )
        return data

    def create(self, validated_data):
        # Extract the 'testcases' and 'choices' data from the validated data
        testcases = validated_data.pop("testcases")
        choices = validated_data.pop("choices")

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

    def update(self, instance, validated_data):
        # sourcery skip: use-named-expression
        # Update the instance fields with the validated data
        instance.text = validated_data.get("text", instance.text)
        instance.question_type = validated_data.get("question_type", instance.question_type)
        instance.code_template = validated_data.get("code_template", instance.code_template)

        # Save the updated instance
        instance.save()

        # Update choices and testcases
        choices = validated_data.get("choices", [])
        testcases = validated_data.get("testcases", [])

        # Update choices
        for choice_data in choices:
            choice_text = choice_data.get("text")
            if choice_text:
                choice = Choice.objects.get(text=choice_text, question=instance)
                choice.text = choice_data.get("text", choice.text)
                choice.is_correct = choice_data.get("is_correct", choice.is_correct)
                choice.save()
            else:
                Choice.objects.get_or_create(question=instance, **choice_data)

        # Update testcases
        for testcase_data in testcases:
            testcase_id = testcase_data.get("id")
            if testcase_id:
                testcase = TestCase.objects.get(id=testcase_id)
                testcase.input_data = testcase_data.get("input_data", testcase.input_data)
                testcase.expected_output = testcase_data.get("expected_output", testcase.expected_output)
                testcase.is_public = testcase_data.get("is_public", testcase.is_public)
                testcase.save()
            else:
                TestCase.objects.get_or_create(question=instance, **testcase_data)

        return instance


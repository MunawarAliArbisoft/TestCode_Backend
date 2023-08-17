from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Assessment, AssessmentResult
from question.models import Question
from .serializers import AssessmentSerializer, AssessmentResultSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrCandidate

from .code_executor import execute_testcases


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class AssessmentResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentResult.objects.all()
    serializer_class = AssessmentResultSerializer
    permission_classes = [IsAuthenticated, IsAdminOrCandidate]


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_assessment(request):
    assessment_id = request.data.get("assessment_id")
    answers = request.data.get("answers")

    assessment = Assessment.objects.get(pk=assessment_id)
    total_score = 0

    for answer_data in answers:
        question_id = answer_data["question_id"]
        question_type = answer_data["question_type"]

        question = Question.objects.get(pk=question_id)

        if question_type == "MCQ":
            selected_choice_id = answer_data["selected_choice_id"]
            correct_choice = question.choices.get(is_correct=True)

            if selected_choice_id == correct_choice.id:
                total_score += 1  # Increment score for correct MCQ answer

        elif question_type == "COD":
            code = answer_data["code"]
            testcases = question.testcases.all()

            for testcase in testcases:
                testcase_input = testcase.input_data
                testcase_output = testcase.expected_output
                result = execute_testcases(bytes(code, 'utf-8'), testcase_input, testcase_output)
                # if all test cases passed then total score += 1

    # calculate the percentage score
    total_questions = assessment.questions.count()
    percentage_score = (total_score / total_questions) * 100

    # AssessmentResult instance with the calculated total_score
    # AssessmentResult.objects.create(
    #     candidate=request.user,
    #     assessment=assessment,
    #     score=float(f"{percentage_score:.2f}"),
    # )

    # Return a response with additional data
    response_data = {
        "message": "Assessment submitted successfully.",
        "percentage_score": percentage_score
    }

    return Response(response_data, status=status.HTTP_201_CREATED)

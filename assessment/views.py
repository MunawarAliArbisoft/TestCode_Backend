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
from .evaluate_assessment import evaluate_assessment, assessment_response


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

    percentage_score, assessment_results = evaluate_assessment(assessment, answers)

    # Return a response with additional data
    response_data = assessment_response(percentage_score, assessment, assessment_results)
    
    # AssessmentResult instance with the calculated total_score
    # AssessmentResult.objects.create(
    #     candidate=request.user,
    #     assessment=assessment,
    #     score=float(f"{percentage_score:.2f}"),
    # )

    return Response(response_data, status=status.HTTP_201_CREATED)

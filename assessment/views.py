from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from question.models import Question
from candidate.permissions import CandidatePermission

from .models import Assessment, AssessmentResult, Answer
from .serializers import AssessmentSerializer, AssessmentResultSerializer, AnswerSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrCandidate

from .evaluate_assessment import evaluate_assessment, assessment_response


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class AssessmentResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentResult.objects.all()
    serializer_class = AssessmentResultSerializer
    http_method_names = ['get', 'retrieve']
    permission_classes = [IsAuthenticated, IsAdminOrCandidate]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, CandidatePermission]


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_assessment(request):
    assessment_id = request.data.get("assessment_id")
    candidate_id = request.user.id

    user_answers = Answer.objects.filter(candidate_id=candidate_id, assessment_id=assessment_id)

    answers = AnswerSerializer(user_answers, many=True).data
    assessment = get_object_or_404(Assessment, id=assessment_id) 

    if user_answers.count() < 2 and assessment.questions.count() >= 2:
        return Response({"message": f"Please attempt at least 3 answers {request.user}","error":"Insufficient answers"}, status=status.HTTP_400_BAD_REQUEST)

    percentage_score, assessment_results = evaluate_assessment(assessment, answers)

    # Return a response with additional data
    response_data = assessment_response(percentage_score, assessment, assessment_results)
    
    # AssessmentResult instance with the calculated total_score
    try:
        AssessmentResult.objects.create(
            candidate=request.user,
            assessment=assessment,
            score=float(f"{percentage_score:.2f}"),
            result = assessment_results,
        )
    except IntegrityError as e:
        return Response({"message": f"This Assessment Already Attempted by {request.user}","error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([IsAdminUser])
def update_question(request, action):
    assessment_id = request.data.get("assessment_id")
    question_id = request.data.get("question_id")

    try:
        assessment = Assessment.objects.get(id=assessment_id)
        question = Question.objects.get(id=question_id)

        if action == "add":
            assessment.questions.add(question)
            message = "Question added successfully."
        elif action == "remove":
            assessment.questions.remove(question)
            message = "Question removed successfully."
        else:
            return Response({"message": "Invalid action."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": message}, status=status.HTTP_200_OK)
    except Assessment.DoesNotExist:
        return Response({"message": "Assessment not found."}, status=status.HTTP_404_NOT_FOUND)
    except Question.DoesNotExist:
        return Response({"message": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

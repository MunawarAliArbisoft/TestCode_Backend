from rest_framework import serializers
from .models import *
from candidate.serializers import CandidateSerializer
from question.serializers import QuestionSerializer

class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = ['id', 'title', 'description', 'date_created', 'date_updated', 'questions']

class AssessmentResultSerializer(serializers.ModelSerializer):
    assessment = AssessmentSerializer()
    candidate = CandidateSerializer()

    class Meta:
        model = AssessmentResult
        fields = ['id', 'score', 'submission_date', 'assessment', 'candidate']

    def to_internal_value(self, data):
        # Extract candidate email and assessment ID from the incoming data
        candidate_email = data['candidate']['email']
        assessment_id = data['assessment']['id']
        
        # Retrieve the Candidate object from the database using the provided email
        try:
            candidate = Candidate.objects.get(email=candidate_email)
        except Candidate.DoesNotExist:
            raise serializers.ValidationError("Candidate does not exist.")
        
        # Retrieve the Assessment object from the database using the provided ID
        try:
            assessment = Assessment.objects.get(id=assessment_id)
        except Assessment.DoesNotExist:
            raise serializers.ValidationError("Assessment does not exist.")
        
        # Create a dictionary containing candidate, assessment, and score
        assessment_result = {
            'candidate': candidate,
            'assessment': assessment,
            'score': data.get('score')
        }

        return assessment_result

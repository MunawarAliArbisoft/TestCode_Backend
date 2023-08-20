from django.db import models

from candidate.models import Candidate
from question.models import Question


class Assessment(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    questions = models.ManyToManyField(Question, related_name="assessments")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class AssessmentResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField()
    result = models.JSONField(null=True)
    submission_date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['candidate', 'assessment'], name='unique_assessment_result')]

    def __str__(self):
        return f"{self.candidate} - {self.assessment} - {self.score}"
    
class Answer(models.Model):
    candidate_id = models.PositiveIntegerField()
    assessment_id = models.PositiveIntegerField()
    question_id = models.PositiveIntegerField()
    question_type = models.CharField(max_length=3)
    selected_choice_id = models.PositiveIntegerField(null=True)
    code = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by Candidate ID {self.candidate_id} for Assessment ID {self.assessment_id}"


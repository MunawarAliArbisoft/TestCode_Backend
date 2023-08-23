from django.db import models

from candidate.models import Candidate
from question.models import Question


class Assessment(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    questions = models.ManyToManyField(Question, related_name="assessments", blank=True)
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

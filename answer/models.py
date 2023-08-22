from django.db import models

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



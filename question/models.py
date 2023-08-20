from django.db import models
from django.core.exceptions import ValidationError

class Question(models.Model):
    QUESTION_TYPES = (
        ("MCQ", "Multiple Choice Question"),
        ("COD", "Coding Question"),
    )
    text = models.TextField()
    question_type = models.CharField(
        max_length=3, choices=QUESTION_TYPES, default="MCQ"
    )
    code_template = models.TextField(blank=True, null=True)  # For coding questions

    class Meta:
        constraints = [models.UniqueConstraint(fields=['text', 'question_type'], name='unique_question')]

    def __str__(self):
        return self.text[:50]  # Return first 50 characters of the question text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['question', 'text'], name='unique_choice')]

    def __str__(self):
        return self.text


class TestCase(models.Model):
    question = models.ForeignKey(
        Question, related_name="testcases", on_delete=models.CASCADE
    )
    input_data = models.TextField()
    expected_output = models.TextField()
    is_public = models.BooleanField(
        default=True
    )  # Public test cases are visible to candidates

    def __str__(self):
        return f"Test case for {self.question}"

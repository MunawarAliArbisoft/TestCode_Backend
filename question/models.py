from django.db import models
from django.template.defaultfilters import slugify

from assessment.models import Assessment


class Question(models.Model):
    QUESTION_TYPES = (
        ("MCQ", "Multiple Choice Question"),
        ("COD", "Coding Question"),
    )

    assessment = models.ForeignKey(
        Assessment, related_name="questions", on_delete=models.CASCADE
    )
    text = models.TextField()
    question_type = models.CharField(
        max_length=3, choices=QUESTION_TYPES, default="MCQ"
    )
    code_template = models.TextField(blank=True, null=True)  # For coding questions
    slug = models.SlugField(max_length=100, unique=True)

    def slug(self):
        return slugify(self.text)

    def __str__(self):
        return self.text[:50]  # Return first 50 characters of the question text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

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

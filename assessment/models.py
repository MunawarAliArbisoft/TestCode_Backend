from django.db import models
from django.template.defaultfilters import slugify

from candidate.models import Candidate

# Create your models here.
class Assessment(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title
    
class AssessmentResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField()
    submission_date = models.DateField()

    def __str__(self):
        return f"{self.candidate} - {self.assessment}"
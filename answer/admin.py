from django.contrib import admin
from .models import Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ["candidate_id", "assessment_id", "question_id", "question_type"]

admin.site.register(Answer, AnswerAdmin)


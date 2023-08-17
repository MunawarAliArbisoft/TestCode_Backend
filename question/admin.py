from django.contrib import admin
from .models import Question, Choice, TestCase


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class TestCaseInline(admin.StackedInline):
    model = TestCase
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, TestCaseInline]
    list_display = ["text", "assessment", "question_type"]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

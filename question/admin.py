from django.contrib import admin
from .models import Question, Choice, TestCase


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class TestCaseInline(admin.StackedInline):
    model = TestCase
    extra = 0

class QuestionInline(admin.TabularInline):
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, TestCaseInline]
    list_display = ["text", "question_type"]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["text", "is_correct", 'question']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

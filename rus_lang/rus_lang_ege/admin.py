from django.contrib import admin
from django.forms import TextInput, Textarea

from django.db import models


from .models import Level, Test, Question, Answer, ExamResult


class LevelAdmin(admin.ModelAdmin):
    list_display = ("id", "number_of_class")


# class TestAdmin(admin.ModelAdmin):
#     list_display = ("id", "title")


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ("id", "question_text", "correct_answer_count")
#     list_editable = ("question_text", "correct_answer_count")
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'20'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
#     }


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer_text",
                    "is_right")


class ExamResultAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "test",
                    "score", "conclusion", "finished_at")


admin.site.register(Level, LevelAdmin)
# admin.site.register(Test, TestAdmin)
# admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ExamResult, ExamResultAdmin)

from django.contrib import admin


from .models import Level, Answer, ExamResult


class LevelAdmin(admin.ModelAdmin):
    list_display = ("id", "number_of_class")


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer_text",
                    "is_right")


class ExamResultAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "test",
                    "score", "conclusion", "finished_at")


admin.site.register(Level, LevelAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ExamResult, ExamResultAdmin)

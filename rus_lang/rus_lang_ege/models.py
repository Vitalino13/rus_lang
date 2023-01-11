from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db import models
from django.urls import reverse_lazy, reverse

User = get_user_model()

CONCLUSION_CHOISES = (
    ("5", "Все супер"),
    ("4", "Ошибки есть,но все-равно молодец"),
    ("3", "Надо приложить усилия для изучения этой темы")
)


class Level(models.Model):
    number_of_class = models.CharField(
        verbose_name="Номер класса",
        help_text="Введите класс или экзамен",
        max_length=150,
    )

    def __str__(self) -> str:
        return self.number_of_class

    def get_absolute_url(self):
        return reverse_lazy('rus_lang_ege:test_page',
                            kwargs={"grade_id": self.id})

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Test(models.Model):
    title = models.CharField(
        verbose_name="Название теста",
        help_text="Введите название теста или его номер",
        max_length=200
    )
    grade = models.ForeignKey(
        "Level",
        verbose_name="Класс",
        help_text="Вы не можете удалить класс,пока у него есть тесты",
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('rus_lang_ege:question_page',
                            kwargs={'test_id': self.id,
                                    'grade_id': self.grade.id})

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    question_text = models.TextField(
        verbose_name="Текст вопроса",
        help_text="Введите вопрос",
    )
    correct_answer_count = models.SmallIntegerField(
        verbose_name="Количество правильных ответов",
        help_text="Введите количество правильных ответов у этого вопроса",
    )
    test = models.ForeignKey(
        "Test",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["id"]


class Answer(models.Model):
    answer_text = models.CharField(
        verbose_name="Ответ",
        help_text="Введите вариант ответа",
        max_length=256,
    )
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
    )
    is_right = models.BooleanField(
        verbose_name="Правильный ответ",
        help_text="Отметьте, если ответ правильный",
    )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["id"]


class ExamResult(models.Model):
    score = models.SmallIntegerField(
        verbose_name="Количество правильных ответов",
        help_text="Количество правильных ответов за тест",
    )
    conclusion = models.CharField(
        verbose_name="заключение",
        choices=CONCLUSION_CHOISES,
        max_length=50
    )
    finished_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время окончания теста",
    )
    test = models.ForeignKey(
        "Test",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"


class QuestionInLine(admin.TabularInline):
    model = Answer


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]
    list_display = ('id', 'question_text', "correct_answer_count", "test")


class TestInline(admin.TabularInline):
    model = Question


@admin.register(Test)
class TestCreateAdmin(admin.ModelAdmin):
    inlines = [TestInline]
    list_display = ('id', 'title', 'grade')
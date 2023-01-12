from django.views.generic import ListView, FormView
from django.shortcuts import get_object_or_404, render
from .models import Level, Test, Question, Answer
from pprint import pprint


class IndexPageList(ListView):
    """Класс для отображения главное страницы, где будет 5-8, ЕГЭ, ОГЭ."""
    model = Level
    template_name = "rus_lang_ege/index.html"


class GradePageList(ListView):
    model = Test
    template_name = "rus_lang_ege/list_of_test.html"
    context_object_name = "test_list"

    def get_queryset(self):
        return Test.objects.filter(grade__id=self.kwargs['grade_id'])


class TestPageList(ListView):
    model = Question
    template_name = "rus_lang_ege/list_of_question.html"
    context_object_name = "question_list"

    def get_queryset(self):
        return Question.objects.filter(test__id=self.kwargs['test_id'])


def vote(request, test_id):
    list_of_question = [q.id for q in Question.objects.filter(test=test_id)]
    answers = {}
    question = Question.objects.get(id=list_of_question[0]).answer_set.all()
    for ans in question:
        ans.is_right
    print(list_of_question)
    answer = dict(request.POST)
    del answer['csrfmiddlewaretoken']
    print(answer)
    return render(request,
                  "rus_lang_ege/list_of_question.html")
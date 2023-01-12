from django.views.generic import ListView
from django.shortcuts import render
from .models import Level, Test, Question


from .utils import check_answer, convert_to_dict, remove_token_key


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
    list_of_question = [q for q in Question.objects.filter(
        test=test_id).values_list(
            'id', "answers__id", "answers__is_right")]
    response = list(request.POST.lists())
    response = remove_token_key(response)
    dict_of_question = convert_to_dict(list_of_question)
    message = "sgds"
    message = check_answer(response, dict_of_question)
    context = {'message': message}
    return render(request,
                  "rus_lang_ege/results.html", context=context)

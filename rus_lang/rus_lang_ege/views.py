from django.views.generic import ListView, FormView
from django.shortcuts import get_object_or_404, render
from .models import Level, Test, Question, Answer


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


def vote(request, question_id):
	# print(request.POST['choice'])
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

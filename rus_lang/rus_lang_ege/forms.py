from django.forms import forms

from .models import Question


class QuestionForm(forms.Form):
    class META:
        model = Question
        fields = ['question', ]

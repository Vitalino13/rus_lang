from django.urls import path

from .views import IndexPageList, GradePageList, TestPageList, vote

app_name = "rus_lang_ege"
urlpatterns = [
    path("", IndexPageList.as_view(), name="index_page"),
    path(
        "grade/<int:grade_id>/",
        GradePageList.as_view(),
        name="test_page"
    ),
    path(
        "grade/<int:grade_id>/test/<int:test_id>/",
        TestPageList.as_view(),
        name="question_page"
        ),
    path('test/<int:test_id>/vote/', vote, name='vote'),

]

from django.urls import path
from .api import ProgrammingLanguagesList, ProgrammingLanguagesDateList

app_name = "data_visualisation"

urlpatterns = [
    path(
        "api/programming-langague/",
        ProgrammingLanguagesList.as_view(),
        name="programming-langague",
    ),
    path(
        "api/programming-langague/date",
        ProgrammingLanguagesDateList.as_view(),
        name="programming-langague-date",
    ),
]

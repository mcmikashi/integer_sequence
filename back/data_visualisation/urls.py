from django.urls import path
from .api import ProgrammingLanguagesList

app_name = "data_visualisation"

urlpatterns = [
    path(
        "api/programming-langague/",
        ProgrammingLanguagesList.as_view(),
        name="programming-langague",
    ),
]

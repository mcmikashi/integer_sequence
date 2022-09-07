from rest_framework import generics
from .models import ProgrammingLanguages
from .serializers import (
    ProgrammingLanguagesSerializer,
    ProgrammingLanguagesDateSerializer,
)


class ProgrammingLanguagesList(generics.ListAPIView):
    """
    List all programming langague with share by date.
    """

    serializer_class = ProgrammingLanguagesSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned programming langague and the share of a given date,
        by filtering against the `date` query parameter in the URL.
        """
        queryset = ProgrammingLanguages.objects.all()
        date = self.request.query_params.get("date")
        if date is not None:
            queryset = queryset.filter(date=date)
        return queryset


class ProgrammingLanguagesDateList(generics.ListAPIView):
    """
    List all distinct date of programming langague instance.
    """

    queryset = ProgrammingLanguages.objects.distinct("date")
    serializer_class = ProgrammingLanguagesDateSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProgrammingLanguages
from .serializers import ProgrammingLanguagesSerializer


class ProgrammingLanguagesList(APIView):
    """
    List all programming langague with share by date.
    """

    def get(self, request, format=None):
        programming_languages = ProgrammingLanguages.objects.all()
        serializer = ProgrammingLanguagesSerializer(
            programming_languages, many=True
        )
        return Response(serializer.data)

from rest_framework.test import APITestCase
from .models import ProgrammingLanguages
from datetime import date
from django.urls import reverse
from rest_framework import status
from .serializers import ProgrammingLanguagesSerializer


class ProgrammingLanguagesTestCase(APITestCase):
    def setUp(self):
        programing_date = date(2022, 4, 24)
        ProgrammingLanguages.objects.create(
            name="python", date=programing_date, share=75.5
        )
        ProgrammingLanguages.objects.create(
            name="php", date=programing_date, share=12.5
        )

    def test_api_list_view(self):
        """Make sure that the api return the good value"""
        url = reverse("data_visualisation:programming-langague")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        queryset = ProgrammingLanguages.objects.all()
        serialized = ProgrammingLanguagesSerializer(queryset, many=True)
        self.assertEqual(response.data, serialized.data)

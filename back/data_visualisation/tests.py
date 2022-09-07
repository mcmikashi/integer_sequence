from rest_framework.test import APITestCase
from .models import ProgrammingLanguages
from datetime import date
from django.urls import reverse
from rest_framework import status
from .serializers import (
    ProgrammingLanguagesSerializer,
    ProgrammingLanguagesDateSerializer,
)


class ProgrammingLanguagesTestCase(APITestCase):
    def setUp(self):
        self.programing_date = date(2022, 4, 1)
        ProgrammingLanguages.objects.create(
            name="python", date=self.programing_date, share=75.5
        )
        ProgrammingLanguages.objects.create(
            name="php", date=self.programing_date, share=12.5
        )

    def test_api_list_view(self):
        """Make sure that the api return the good value"""
        url = reverse("data_visualisation:programming-langague")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

        queryset = ProgrammingLanguages.objects.all()
        serialized = ProgrammingLanguagesSerializer(queryset, many=True)
        self.assertEqual(response.data["results"], serialized.data)

    def test_api_list_view_filtering_by_date(self):
        """Make sure that the api return the good value"""

        # Add new a new object with a diffrent date
        new_date = date(2022, 2, 1)
        ProgrammingLanguages.objects.create(
            name="javascript", date=new_date, share=30
        )

        url = reverse("data_visualisation:programming-langague")
        # Add the querypram to the url
        url_with_query_param = f"{url}?date={new_date}"
        response = self.client.get(url_with_query_param)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

        queryset = ProgrammingLanguages.objects.all().filter(date=new_date)
        serialized = ProgrammingLanguagesSerializer(queryset, many=True)
        self.assertEqual(response.data["results"], serialized.data)

    def test_api_list_view_date(self):
        """Make sure that the api return the good value"""
        url = reverse("data_visualisation:programming-langague-date")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

        queryset = ProgrammingLanguages.objects.distinct("date")
        serialized = ProgrammingLanguagesDateSerializer(queryset, many=True)
        self.assertEqual(response.data["results"], serialized.data)

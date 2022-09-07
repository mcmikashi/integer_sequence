from rest_framework import serializers
from .models import ProgrammingLanguages


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = ["date", "share", "name"]


class ProgrammingLanguagesDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = ["date"]

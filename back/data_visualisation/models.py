from django.db import models


class BaseDataVisulation(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    share = models.FloatField()

    class Meta:
        abstract = True
        ordering = ["date", "share"]


class ProgrammingLanguages(BaseDataVisulation):
    pass

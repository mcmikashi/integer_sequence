from django.urls import path
from .api import FibbonaciView

app_name = 'sequence'

urlpatterns = [
    path('api/fibonacci/<int:index>', FibbonaciView.as_view(), name='fibonacci')
]
from django.urls import path
from .api import FibonacciView

app_name = 'sequence'

urlpatterns = [
    path('api/fibonacci/<int:index>', FibonacciView.as_view(), name='fibonacci')
]
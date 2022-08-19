from django.urls import path
from .api import FibonacciView, LucasView

app_name = 'sequence'

urlpatterns = [
    path('api/fibonacci/<int:index>', FibonacciView.as_view(), name='fibonacci'),
    path('api/lucas/<int:index>', LucasView.as_view(), name='lucas')

]
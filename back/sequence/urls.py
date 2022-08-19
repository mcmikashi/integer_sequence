from django.urls import path
from .api import FibonacciView, LucasView,  DyingRabbitsView

app_name = 'sequence'

urlpatterns = [
    path('api/fibonacci/<int:index>', FibonacciView.as_view(), name='fibonacci'),
    path('api/lucas/<int:index>', LucasView.as_view(), name='lucas'),
    path('api/rabbits/<int:index>', DyingRabbitsView.as_view(), name='dying_rabbits')

]

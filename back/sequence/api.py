from operator import index
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .utils import Update_Recursion_Limit, fibonacci, lucas

class SequenceBaseView(APIView):
    """Base view for sequence API"""
    # settting the default max recursion litmit
    max_recursion_limit = 2000
    # setting the default function variable
    sequence_function = lambda index : index
    # setting the default error message
    default_error_message = \
        "You send an invalid index.Index SHOULD be between 0 and 1000 included."

    def get(self, request, index):
        """
        Return the value of the default function
        """
        with Update_Recursion_Limit(self.max_recursion_limit):
            try:
                result = self.sequence_function(index)
            except ValueError:
                raise NotFound(
                    detail=self.default_error_message,
                    code=404)
        return Response({'result':result})


class FibonacciView(SequenceBaseView):
    """
    View to return the value of the fibbonaci sequence at the index
    """
    sequence_function =  staticmethod(fibonacci)

class LucasView(SequenceBaseView):
    """
    View to return the value of the lucas sequence at the index
    """
    sequence_function =  staticmethod(lucas)
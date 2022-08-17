from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .utils import Update_Recursion_Limit, fibonacci

class FibbonaciView(APIView):
    """
    View to return the value of the fibbonaci sequence at the index
    """

    def get(self, request, index):
        """
        Return the value of fibonacci function
        """
        with Update_Recursion_Limit(2000):
            try:
                result = fibonacci(index)
            except ValueError:
                raise NotFound(
                    detail="You send an invalid index.Index SHOULD "
                           "be between 0 and 1000 included.",
                    code=404)
        return Response({'result':result})

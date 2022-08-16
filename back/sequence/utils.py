import sys
from functools import cache

class Update_Recursion_Limit:
    """
    Allow to change the recursion limit
    """
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)


@cache
def fibonacci(index: int) -> int:
    """This is the rercusive function of the fibonacci suite
    Args:
        index (int): the index of fibonacci
    Returns:
        [int]: the number of fibonacci at the index
    """
    if not isinstance(index,int) or index not in range(1001):
        raise ValueError
    else:
        if index in [0, 1]:
            return index
        return fibonacci(index-1) + fibonacci(index-2)

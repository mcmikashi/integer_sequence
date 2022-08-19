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
    """This is the rercusive function of the fibonacci sequence
    Args:
        index (int): the index of fibonacci sequence
    Returns:
        [int]: the result of fibonacci  sequence at the index
    """
    if not isinstance(index,int) or index not in range(1001):
        raise ValueError
    else:
        if index in [0, 1]:
            return index
        return fibonacci(index-1) + fibonacci(index-2)

@cache
def lucas(index: int) -> int:
    """This the rercusive function of the lucas sequence
    Args:
        index (int): the index of lucas sequence
    Returns:
        [int]: the result of lucas sequence at the index
    """
    if not isinstance(index,int) or index not in range(1001):
        raise ValueError
    if index == 0:
        return 2
    if index == 1:
        return 1
    return lucas(index-1) + lucas(index-2)

@cache
def dying_rabbits(index: int) -> int:
    """This the rercusive function of the dying rabbit sequence
    Args:
        index (int): the index of dying rabbit sequence
    Returns:
        [int]: the result of dying rabbit  sequence at the index
    """
    if not isinstance(index,int) or index not in range(1001):
        raise ValueError
    if index in range(13):
        if index in [0, 1, 2]:
            return 1
        else:
            return dying_rabbits(index-1) + dying_rabbits(index-2)
    else:
        return ((dying_rabbits(index-1) + dying_rabbits(index-2)) 
                - dying_rabbits(index-13))

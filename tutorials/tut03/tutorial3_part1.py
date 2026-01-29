"""CSC111 Tutorial 3: Induction and Recursion

Module Description
==================
This module contains the specifications for various recursive functions on nested lists.
Your task in this part of the tutorial is to implement all of these functions.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC111 Teaching Team
"""
from typing import Optional

from python_ta.contracts import check_contracts


# For your reference, this is the "sum_nested" function from lecture.
@check_contracts
def sum_nested(nested_list: int | list) -> int:
    """Return the sum of the given nested list.
    """
    if isinstance(nested_list, int):
        return nested_list
    else:
        # Version 1: using a loop
        sum_so_far = 0
        for sublist in nested_list:
            sum_so_far += sum_nested(sublist)
        return sum_so_far

        # Version 2: using a comprehension and the built-in sum function
        # return sum(sum_nested(sublist) for sublist in nested_list)


@check_contracts
def all_less_than(nested_list: int | list, n: int) -> bool:
    """Return whether every integer in nested_list is less than n.

    >>> all_less_than(10, 3)
    False
    >>> all_less_than([1, 2, [1, 2], 4], 10)
    True
    >>> all_less_than([], 0)
    True
    """
    if isinstance(nested_list, int):
        return nested_list < n
    else:
        return all(all_less_than(sublist, n) for sublist in nested_list)


@check_contracts
def add_n(nested_list: int | list, n: int) -> int | list:
    """Return a new nested list where n is added to every item in nested_list.

    >>> add_n(10, 3)
    13
    >>> add_n([1, 2, [1, 2], 4], 10)
    [11, 12, [11, 12], 14]
    """
    if isinstance(nested_list, int):
        return nested_list + n
    else:
        return [add_n(sublist, n) for sublist in nested_list]


@check_contracts
def first_at_depth(nested_list: int | list, d: int) -> Optional[int]:
    """Return the first (leftmost) integer in nested_list at depth d.

    Return None if there is no integer at depth d in nested_list

    Hint: review items_at_depth from lecture!

    Preconditions:
        - d >= 0

    >>> first_at_depth(100, 0)
    100
    >>> first_at_depth(100, 3) is None
    True
    >>> first_at_depth([10, [[20]], [30, 40]], 2)
    30
    >>> first_at_depth([10, [[20]], [30, 40]], 3)
    20
    >>> first_at_depth([10, [[20]], [30, 40]], 4) is None
    True
    """
    if isinstance(nested_list, int):
        if d == 0:
            return nested_list
        else:
            return None
    else:
        if d == 0:
            return None
        for item in nested_list:
            result = first_at_depth(item, d - 1)
            if result is not None:
                return result
        return None


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120
    # })

"""CSC111 Winter 2026 Prep 2: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains the implementation of linked lists with the append method
and updated initializer from the prep reading.

There are two additional methods at the bottom of the class that we have started.
Your first task is to implement EACH method based on the method header and description.

Your second task is to write a set of tests for each of the methods, as described at the bottom
of this file. This is good review of how to write unit tests in Python from CSC110, which you'll
need to do throughout this course.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC111 Teaching Team
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional
from python_ta.contracts import check_contracts

import pytest  # You'll need to use pytest.raises in your tests (see below)


@check_contracts
@dataclass
class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[_Node] = None  # By default, this node does not link to any other node


@check_contracts
class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for item in items:
            self.append(item)

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def append(self, item: Any) -> None:
        """Append item to the end of this list.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.append(4)
        >>> lst.to_list()
        [1, 2, 3, 4]
        """
        new_node = _Node(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    ############################################################################
    # Prep exercises start here
    ############################################################################
    def remove_first(self) -> Any:
        """Remove and return the first element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_first()
        1
        >>> lst.to_list()
        [2, 3]
        >>> lst.remove_first()
        2
        >>> lst.remove_first()
        3
        """
        if self._first is None:
            raise IndexError("Empty")
        first_node = self._first
        self._first = self._first.next
        return first_node.item

    def remove_last(self) -> Any:
        """Remove and return the last element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_last()
        3
        >>> lst.to_list()
        [1, 2]
        >>> lst.remove_last()
        2
        >>> lst.remove_last()
        1

        IMPLEMENTATION HINTS:
            1. You'll need to modify the linked list traversal pattern to reach
               the *second-last node*.
            2. It's okay to have separate cases (using if statements) for size-0
               and size-1 linked lists.
        """

        if self._first is None:
            raise IndexError("Empty")
        if self._first.next is None:
            return self.remove_first()
        curr = self._first
        while curr.next.next is not None:
            curr = curr.next
        v = curr.next.item
        curr.next = None
        return v


################################################################################
# Test cases
################################################################################
# Write unit tests for each of the two LinkedList methods you implemented above.
# Your tests should cover various cases for possible linked list lengths (including
# empty linked lists!) and should check both for mutation and the correct return value.
# You can use the LinkedList.to_list method to check the values in the linked list.
# Each unit test should have a docstring containing a brief description of the test.
#
# To review how to write unit tests using pytest (including testing for errors being raised),
# please consult
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html.
#
# WARNING: your test function names MUST start with "test_", otherwise they won't
# be detected as unit tests by pytest, and therefore won't be run.


def test_remove_first_1() -> None:
    """Test method remove_first with a LinkedList with multiple elements"""
    lst = LinkedList([1, 2, 3])
    removed = lst.remove_first()

    assert removed == 1
    assert lst.to_list() == [2, 3]


def test_remove_first_2() -> None:
    """Test method remove_first with a LinkedList with single element"""
    lst = LinkedList([10])
    removed = lst.remove_first()

    assert removed == 10
    assert lst.to_list() == []


def test_remove_first_3() -> None:
    """Test method remove_first with an empty LinkedList"""
    lst = LinkedList([])

    with pytest.raises(IndexError):
        lst.remove_first()


def test_remove_last_1() -> None:
    """Test method remove_last with a LinkedList with multiple elements"""
    lst = LinkedList([1, 2, 3])
    removed = lst.remove_last()

    assert removed == 3
    assert lst.to_list() == [1, 2]


def test_remove_last_2() -> None:
    """Test method remove_last with a LinkedList with single element1"""
    lst = LinkedList([99])
    removed = lst.remove_last()

    assert removed == 99
    assert lst.to_list() == []


def test_remove_last_3() -> None:
    """Test method remove_last with a LinkedList with multiple elements step by step"""
    lst = LinkedList([1, 2, 3])

    assert lst.remove_last() == 3
    assert lst.remove_last() == 2
    assert lst.remove_last() == 1
    assert lst.to_list() == []


def test_remove_last_empty() -> None:
    """Test method remove_last with an empty LinkedList"""
    lst = LinkedList([])

    with pytest.raises(IndexError):
        lst.remove_last()


if __name__ == '__main__':
    # Reminder: This runs pytest on the test cases you've added to this file.
    pytest.main(['prep2.py', '-v'])

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    # You can use "Run file in Python Console" to run both pytest and PythonTA,
    # and then also test your methods manually in the console.
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
    })

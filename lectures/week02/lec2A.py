from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Iterable
import math


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


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing
        the given items.
        >>> linky = LinkedList([1, 2, 3])
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

    def sum_items(self) -> int:
        """Return the sum of items in the linked list.
        """
        sum_so_far = 0
        curr = self._first

        while curr is not None:
            sum_so_far += curr.item
            curr = curr.next

        return sum_so_far

    def maximum(self) -> float:
        """Return the maximum element in this linked list.

        Preconditions:
            - every element in this linked list is a float
            - this linked list is not empty

        >>> linky = LinkedList()
        >>> node3 = _Node(30.0)
        >>> node2 = _Node(-20.5, node3)
        >>> node1 = _Node(10.1, node2)
        >>> linky._first = node1
        >>> linky.maximum()
        30.0
        """
        # Implementation note: as usual for compute maximums,
        # import the math module and initialize your accumulator
        # to -math.inf (negative infinity).
        max_so_far = -math.inf
        curr = self._first

        while curr is not None:
            if curr.item > max_so_far:
                max_so_far = curr.item

            curr = curr.next

        return max_so_far

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        >>> linky = LinkedList()
        >>> linky.__contains__(10)
        False
        >>> node2 = _Node(20)
        >>> node1 = _Node(10, node2)
        >>> linky._first = node1
        >>> linky.__contains__(20)
        True
        """
        curr = self._first

        while curr is not None:
            if curr.item == item:
                # We've found the item and can return early.
                return True

            curr = curr.next

        # If we reach the end of the loop without finding the item,
        # it's not in the linked list.
        return False

    def __getitem__(self, i: int) -> Any:
        """Return the item stored at index i in this linked list.

        Raise an IndexError if index i is out of bounds.

        Preconditions:
            - i >= 0
        """
        curr = self._first
        curr_index = 0

        while curr is not None:
            if curr_index == i:
                return curr.item

            curr_index += 1
            curr = curr.next
        assert curr is None or curr_index == i
        if curr is None:
            raise IndexError
        else:
            return curr.item

    def append(self, item: Any) -> None:
        new_node = _Node(item)
        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            # curr is the last node in this LinkedList
            assert curr is not None and curr.next is None
            curr.next = new_node

    def insert(self, i: int, item: Any) -> None:
        """Insert the given item at index i in this list.
        Raise IndexError if i > len(self).
        """
        if i < 0:
            raise IndexError

        new_node = _Node(item)

        # Case 1: insert at front
        if i == 0:
            new_node.next = self._first
            self._first = new_node
            return

        # Traverse to node at index i - 1
        curr = self._first
        curr_index = 0

        while curr is not None:
            if curr_index == i - 1:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr_index += 1
            curr = curr.next

        # If we reach here, i > len(self)
        raise IndexError

    def pop(self, i: int) -> Any:
        """Remove and return the item at index i.
        Raise IndexError if i >= len(self).
        Preconditions:
        - i >= 0
        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.to_list()
        [1, 10, 200]
        """
        if self._first is None:
            raise IndexError
        if i == 0:
            value = self._first.item
            self._first = self._first.next
            return value

        curr = self._first
        curr_index = 0
        while curr.next is not None:
            if curr_index == i - 1:
                value = curr.next.item
                curr.next = curr.next.next
                return value
            curr = curr.next
            curr_index += 1

        raise IndexError

    def remove(self, item: Any) -> None:
        """Remove the first occurrence of item from the li
        Raise ValueError if the item is not found in the l
        >>> lst = LinkedList([10, 20, 30, 20])
        >>> lst.remove(20)
        >>> lst.to_list()
        [10, 30, 20]
        """
        if self._first is None:
            raise ValueError
        prev, curr = None, self._first
        while curr is not None:
            if curr.item == item:
                if prev is None:
                    self._first = curr.next
                else:
                    prev.next = curr.next
                return
            prev, curr = curr, curr.next
        raise ValueError

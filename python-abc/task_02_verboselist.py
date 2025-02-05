#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends
the built-in list class and adds verbose output
for certain operations.
    """


class VerboseList(list):
    def append(self, item):
        """
        Append an item to the list and print a message.
        """

        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """
        Extend the list by appending elements from the iterable
        and print a message.
        """
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list
        and print a message.
        """
        if item not in self:
            print(f"Item [{item}] not found in the list.")
        else:
            print(f"Removed [{item}] from the list.")
            super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given position in the
        list and print a message. If no index is specified,
        removes and returns the last item in the list.
        """
        try:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        except IndexError:
            print("Cannot pop from an empty list or invalid index")

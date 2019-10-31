#!/usr/bin/env python3
"""
Shell Sorting Algorithm uses h-window size to skim through the array and sort
then it reduces the window size in some order and then again sort the array
with elements on its index unless it reaches 1 where it acts as an insertion
sort

"""


class Shell:
    """
    Shell Sort class implementation use sort method to sort and return array
    """
    @staticmethod
    def sort(array):
        """
        Sorts the input unsorted array and returns the sorted array
        Input: array -> list of integers
        Output: array -> list of sorted integers
        """
        N = len(array)
        h = 1
        # Populate the h-size
        while h < N//3:
            h = 3*h + 1

        while h >= 1:
            i = h
            while i < N:
                j = i
                while j >= h:
                    if array[j] < array[j-h]:
                        temp = array[j]
                        array[j] = array[j-h]
                        array[j-h] = temp
                    j -= h
                i += 1

            h //= 3
        return array


if __name__ == '__main__':
    ARRAY = [2, 3, 4, 0, 1, 5]
    assert Shell.sort(ARRAY) == [0, 1, 2, 3, 4, 5]

"""
56. Merge Intervals
Difficulty: Medium
Topic: Array, Divide and Conquer, Sorting
Link: https://leetcode.com/problems/merge-intervals/

Approach:
    Use merge sort to sort intervals by their starting values.

    First, implement merge_sorted_lists() to merge two sorted
    lists based on a given key, and merge_sort() to recursively
    divide the intervals into halves and sort them.

    After sorting:
        1. Initialize new_intervals with the first interval.
        2. Iterate through the remaining sorted intervals.
        3. If the current interval does not overlap with the last
           merged interval, append it to new_intervals and update idx.
        4. Otherwise, merge the intervals by updating the ending
           value to the maximum of both ending values.

    Return new_intervals containing all merged intervals.

Complexity:
    Time:  O(n log n)  # Merge sort dominates the overall time
    Space: O(n)        # Temporary lists and recursive merge sort
"""

from typing import List

class Solution:
    def merge_sorted_lists(self, left, right, key):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def merge_sort(self, arr, key=lambda x: x):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid], key)
        right = self.merge_sort(arr[mid:], key)

        return self.merge_sorted_lists(left, right, key)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort using merge sort
        sorted_intervals = self.merge_sort(
            intervals, key=lambda x: x[0]
        )

        # Step 2: Merge overlapping intervals
        new_intervals = [sorted_intervals[0]]
        idx = 0

        for i in range(1, len(sorted_intervals)):
            current = sorted_intervals[i]

            # If no overlap, append current interval
            if new_intervals[idx][1] < current[0]:
                new_intervals.append(current)
                idx += 1

            # If overlap, merge intervals
            else:
                new_intervals[idx][1] = max(
                    new_intervals[idx][1], current[1]
                )

        return new_intervals

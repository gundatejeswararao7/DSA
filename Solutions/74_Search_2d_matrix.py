"""
74. Search a 2D Matrix
Difficulty: Medium
Topic: Array, Binary Search, Matrix
Link: https://leetcode.com/problems/search-a-2d-matrix/

Approach:
    First, use binary search on the rows to identify the row that
    may contain the target.
    Compare the target with the first and last elements of the middle row.
    If the target lies within that range, perform another binary search
    on that row using the binary_search() helper function.
    If the target is smaller than the first element, search the upper rows.
    Otherwise, search the lower rows.
    Return False if the target is not found.

Complexity:
    Time:  O(log m + log n), where m is the number of rows and n is
           the number of columns
    Space: O(1) auxiliary space
"""

class Solution:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.binary_search(matrix[mid], target)

            elif target < matrix[mid][0]:
                right = mid - 1

            else:
                left = mid + 1

        return False

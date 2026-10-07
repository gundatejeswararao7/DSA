"""
4. Median of Two Sorted Arrays
Difficulty: Hard
Topic: Array, Sorting
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Approach:
    Combine both arrays into one array and sort it.
    If the total number of elements is even, take the average
    of the two middle elements. If it is odd, return the middle
    element directly.

Complexity:
    Time:  O(n log n)
    Space: O(n)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()

        if len(nums1) % 2 == 0:
            median = (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
            return median
        else:
            median = nums1[len(nums1) // 2]
            return median

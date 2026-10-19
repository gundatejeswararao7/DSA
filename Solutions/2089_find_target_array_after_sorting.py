"""
2089. Find Target Indices After Sorting Array
Difficulty: Easy
Topic: Array, Counting, Sorting
Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/

Approach:
    Count the numbers smaller than target (lt) and the numbers equal
    to target (eq).
    After sorting, all numbers smaller than target appear first, so
    the target starts at index lt.
    Generate indices from lt to lt + eq - 1 using range().
    Return the list of target indices without actually sorting nums.

Complexity:
    Time:  O(n + k), where n is the length of nums and k is the number
           of target occurrences
    Space: O(k) for the output list
"""

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lt = eq = 0

        for x in nums:
            if x < target:
                lt += 1
            elif x == target:
                eq += 1

        return list(range(lt, lt + eq))

"""
1. Two Sum
Difficulty: Easy
Topic: Junior, Array, Hash Table
Link: https://leetcode.com/problems/two-sum/

Approach:
    Use Top-Down Dynamic Programming with memoization.
    At each index, keep track of the current parenthesis balance.
    '(' increases the balance, ')' decreases it, and '*' can be treated
    as '(', ')' or an empty string. If the balance becomes negative,
    the string cannot be valid. At the end, the balance must be 0.
    Store each (index, balance) result in memo to avoid recalculating
    the same state.

Complexity:
    Time:  O(n^2)
    Space: O(n^2)
    can be solved in O(n) using Two pointers
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for  j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]

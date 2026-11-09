"""
80. Remove Duplicates from Sorted Array II
Medium
Topic: Array, Two Pointers

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Approach:
- Since the array is sorted, duplicates appear consecutively.
- Use i to traverse the array and d to maintain the position for the next valid element.
- Allow each element to appear at most twice.
- Copy an element when it differs from the previous element or the element two positions before the current valid position.
- Return d as the length of the modified array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        i = 0
        d = 0

        while i < len(nums):
            if i == 0:
                nums[d] = nums[i]
                d += 1

                if len(nums) > 1 and nums[i] == nums[i + 1]:
                    nums[d] = nums[i]
                    d += 1

                i += 1
                continue

            if i == len(nums) - 1:
                if nums[i] != nums[i - 1] or (d > 1 and nums[i] != nums[d - 2]):
                    nums[d] = nums[i]
                    d += 1

                i += 1
                continue

            if nums[i] != nums[i - 1] or (d > 1 and nums[i] != nums[d - 2]):
                nums[d] = nums[i]
                d += 1

            i += 1

        return d

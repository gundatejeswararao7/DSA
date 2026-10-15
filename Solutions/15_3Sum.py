
"""
15. 3Sum
Difficulty: Medium
Topic: Array, Two Pointers, Sorting
Link: https://leetcode.com/problems/3sum/

Approach 1: Using a Set
    Sort the array and fix each element nums[i]. Use two pointers,
    left and right, to find pairs whose sum equals -nums[i].
    If the total is zero, store the triplet as a tuple in a set
    to avoid duplicate triplets. Move both pointers after finding
    a valid triplet. Finally, convert the tuples into lists.

Complexity:
    Time:  O(n^2)
    Space: O(n)

Approach 2: Skipping Duplicates
    Sort the array and fix each element nums[i]. Skip duplicate
    values of nums[i]. Use two pointers to find triplets whose sum
    is zero. When a valid triplet is found, append it to the result
    and skip duplicate values at both pointers. This avoids storing
    triplets in a set.

Complexity:
    Time:  O(n^2)
    Space: O(n) including the output; O(1) auxiliary space
    excluding the output and sorting implementation.

"""

# Approach 1: Using a Set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]

                if val == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1

        return [list(triplet) for triplet in result]


# Approach 2: Skipping Duplicates
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]

                if val == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif val > 0:
                    right -= 1
                else:
                    left += 1

        return result

```python
"""
11. Container With Most Water
Difficulty: Medium
Topic: Array, Two Pointers, Greedy
Link: https://leetcode.com/problems/container-with-most-water/

Approach:
    Use two pointers, left at the beginning and right at the end
    of the array. Calculate the area using the minimum of the two
    heights multiplied by the distance between them. Update max_area
    whenever a larger area is found. Move the pointer with the smaller
    height inward because it limits the water capacity. Repeat until
    both pointers meet, then return max_area.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return max_area
```

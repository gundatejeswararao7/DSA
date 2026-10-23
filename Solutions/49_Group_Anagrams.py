"""
49. Group Anagrams
Difficulty: Medium
Topic: Array, Hash Table, String, Sorting
Link: https://leetcode.com/problems/group-anagrams/

Approach:
    Create a dictionary to group anagrams using sorted strings as keys.
    For each string, sort its characters and join them to create a key.
    If the key already exists, append the string to its group.
    Otherwise, create a new group containing that string.
    Collect all dictionary values and return them as the result.

Complexity:
    Time:  O(n * k log k), where n is the number of strings and k is
           the maximum length of a string
    Space: O(n * k) for storing the groups and dictionary
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for s in strs:
            sorted_str = "".join(sorted(s))

            if sorted_str in group_anagrams:
                group_anagrams[sorted_str].append(s)
            else:
                group_anagrams[sorted_str] = [s]

        anagrams_list = []

        for values in group_anagrams.values():
            anagrams_list.append(values)

        return anagrams_list

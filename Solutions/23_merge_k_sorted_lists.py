"""
23. Merge k Sorted Lists
Difficulty: Hard
Topic: Linked List, Divide and Conquer, Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Approach:
    Use a helper function merge_lists() to merge two sorted linked lists.
    Create a dummy node and compare the values of both lists, attaching
    the smaller node to the result each time.
    Attach any remaining nodes after one list becomes empty.
    In mergeKLists(), start with the first list and merge each subsequent
    list into the result one by one.
    Return the final merged sorted linked list.

Complexity:
    Time:  O(N * k), where N is the total number of nodes and k is the
           number of linked lists
    Space: O(1) auxiliary space, excluding the output list
"""

# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_lists(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1 is not None:
            curr.next = l1

        if l2 is not None:
            curr.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        result = lists[0]

        for i in range(1, len(lists)):
            result = self.merge_lists(result, lists[i])

        return result

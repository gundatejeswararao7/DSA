"""
24. Swap Nodes in Pairs
Difficulty: Medium
Topic: Linked List, Recursion, Pointer Manipulation
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Approach:
    Use a dummy node before the head to simplify swapping.
    Maintain prev as the node before the current pair and curr as the
    first node of the pair.
    Connect prev to the second node, connect the first node to the node
    after the pair, and connect the second node to the first node.
    Move prev and curr forward to process the next pair.
    Return dummy.next as the new head.

Complexity:
    Time:  O(n), where n is the number of nodes
    Space: O(1) auxiliary space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = head
        prev = dummy

        while curr is not None and curr.next is not None:
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = curr

            prev = curr
            curr = curr.next

        return dummy.next

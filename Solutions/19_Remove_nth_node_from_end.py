"""
19. Remove Nth Node From End of List
Difficulty: Medium
Topic: Linked List, Two Passes
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Approach:
    First, traverse the linked list to count the total number of nodes.
    Calculate the position from the beginning using count - n.
    If the position is 0, remove the head by returning head.next.
    Otherwise, traverse to the node just before the target node and
    update its next pointer to skip the target node.
    Return the updated head.

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        key = count - n

        if key == 0:
            return head.next

        curr = head

        while key - 1:
            curr = curr.next
            key -= 1

        curr.next = curr.next.next

        return head

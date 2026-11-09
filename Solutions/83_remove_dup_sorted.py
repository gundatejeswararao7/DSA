"""
83. Remove Duplicates from Sorted List
Easy
Topic: Linked List

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Approach:
- Traverse the sorted linked list using curr.
- If the current node and next node have the same value, delete the next node by updating curr.next.
- Otherwise, move curr to the next node.
- Return the head of the modified list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head

        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

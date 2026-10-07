"""
2. Add Two Numbers
Difficulty: Medium
Topic: Linked List, Math
Link: https://leetcode.com/problems/add-two-numbers/

Approach:
    Traverse both linked lists at the same time and add their values
    along with the carry from the previous addition. Create a new node
    using Sum % 10 and update the carry using Sum // 10. Continue until
    both lists are completely traversed. If a carry remains at the end,
    add one more node.

Complexity:
    Time:  O(max(n, m))
    Space: O(max(n, m))
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carry = 0
        current = dummy

        while l1 or l2:
            Sum = carry

            if l1:
                Sum += l1.val
                l1 = l1.next

            if l2:
                Sum += l2.val
                l2 = l2.next

            new_node = ListNode(Sum % 10)
            carry = Sum // 10

            current.next = new_node
            current = current.next

        if carry:
            new_Node = ListNode(carry)
            current.next = new_Node

        return dummy.next

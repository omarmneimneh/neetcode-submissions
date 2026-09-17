# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = res = ListNode(0)

        while carry or l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            carry += x + y
            curr.next = ListNode(carry%10)
            carry = carry // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        return res.next
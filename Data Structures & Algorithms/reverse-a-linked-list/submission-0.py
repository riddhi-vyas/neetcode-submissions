# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        prev = None
        next_ref = None
        while current:
            next_ref = current.next
            current.next = prev
            prev = current
            current = next_ref
        return prev
#time comp: O(n)
#space comp: O(1)
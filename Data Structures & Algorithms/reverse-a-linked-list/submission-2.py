#Time comp: O(n), Space comp: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        #initialize 3 ptrs
        curr = head
        prev = None
        next_ref = None
        while curr:
            next_ref = curr.next
            curr.next = prev
            prev = curr
            curr = next_ref
        return prev

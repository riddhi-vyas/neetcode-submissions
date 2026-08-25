# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time comp: O(L) where L is the length of the linked list. We traverse the list with the two-pointer technique at most a constant number of passes over the nodes., Space comp: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        # Initialize dummy node and point its next to head
        dummy = ListNode(-1, head)

        #Initialize 2 ptrs and set values to dummy node
        ptr1 = dummy
        ptr2 = dummy

        #update ptr2 for n times
        for i in range(n):
            ptr2 = ptr2.next
        
        #update both ptr1 and ptr2 until ptr2's next is None
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        # ptr1.next is out nth node from list -> update next of ptr1 to remove nth node
        ptr1.next = ptr1.next.next
        return dummy.next
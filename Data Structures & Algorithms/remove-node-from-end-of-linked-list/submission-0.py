# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1. create a dummy node and point dummy's next to head
        dummy = ListNode(-1, head) # -1 is val of node and head is next ptr for dummy

        #2. Initialize 2 ptrs
        ptr1 = dummy
        ptr2 = dummy

        # 3. Move ptr2 n-spaces ahead
        for i in range(n):
            ptr2 = ptr2.next
        
        #4. Move both ptrs, until next of ptr2 is Null
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        #5. we now have to remove ptr1.next
        ptr1.next = ptr1.next.next

        return dummy.next
#time comp: O(L), L is the length of linkedlist
#spcae comp: O(1)
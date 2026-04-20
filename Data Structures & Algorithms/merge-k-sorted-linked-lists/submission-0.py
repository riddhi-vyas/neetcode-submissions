# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        for i in range(1, n):
            lists[i] = self.mergeTwoLists(lists[i-1], lists[i])
        return lists[-1] # Because the loop finishes at the end of the array, 
                         # the fully merged list representing all k lists is now
                         #-sitting at the very last index[-1].

    #Helper function - logic for merging two sorted
    def mergeTwoLists(self, l1, l2) -> Optional[ListNode]:
        # edge case
        if not l1:
            return l2
        if not l2:
            return l1
        # initialize a dummy node
        dummy = ListNode(-1)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next
#time comp: O(N*k), N is total nodes across all k lists
#space comp: O(1)
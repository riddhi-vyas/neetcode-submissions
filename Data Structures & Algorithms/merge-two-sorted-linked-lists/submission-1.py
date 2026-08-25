# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time comp: O(m+n), m is size of list1, n is size of list2, Space comp: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        #create a dummy node -> make it current
        dummy = ListNode(-1)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next # Always update current
        # Check if any of list1 or list is non-empty -> Attach whatever remains
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge case
        if not list1:
            return list2
        if not list2:
            return list1
        # initialize a dummy node
        dummy = ListNode(-1)
        current = dummy
        #iterate over list1 and list2 and merge them
        while list1 and list2:
            if list1.val < list2.val: # if list1's val is smaller -> append it to current
                current.next = list1
                list1 = list1.next # update list1's head
            else: # if list2's val is smaller -> append list2 to current
                current.next = list2
                list2 = list2.next #update list2's head
            current = current.next # update current always
        #check if any of list1 or list2 is non-empty -> if yes -> append to current
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next
#time comp: O(m+n), m and n are lengths of list1 and list2
#space comp: O(1), temp variables are fixed size(current, dummy) which doesn't take any memory and we merged two lists in-place without using extra storage
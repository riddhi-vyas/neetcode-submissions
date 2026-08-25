# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Approach: 1) find middle item from list + create 2 sub-lists
         # 2) Reverse 2nd list
         # 3) Merge two list (1st sublist + 2nd(reversed) sub-list)
#Time comp: O(n), process of finding the middle takes O(n/2),
           #reversing the second half takes O(n/2),
           #and merging also takes O(n/2), all of which sum up to O(n)
# Space comp: O(1), in-place merging
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        #step1 - find middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # after this iteration, we got values of slow and fast
        # -> slow is the middle item (It also is the last node in first sub-list)
        # -> slow.next is the first node in 2nd sub-list

        #step2 - reverse 2nd list
        current = slow.next #slow.next is first node in 2nd sub-list
        prev = None
        next_node = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        # after this iteration, prev is our reversed list2 & first list's tail node = slow
        # need to point next of tail to None to seperate 2 lists
        slow.next = None

        #step3 - Merge 2 lists
        head1 = head
        head2 = prev
        while head2:
            #store next pointers before moving forward
            next1 = head1.next
            next2 = head2.next
            # Merge
            head1.next = head2
            head2.next = next1
            #update heads
            head1 = next1
            head2 = next2
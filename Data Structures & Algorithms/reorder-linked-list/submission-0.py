#logic: find middle item from list -> cut list into two sub-list -> reverese 2nd list
# -> merge list and and list2(reversed)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # 1. Find middle elem from list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # once the slow and fast ptrs have values:
        # -> slow would be the middle elem (Also the last elem in first sub-list)
        # -> slow.next would be the first elem of second sub-list
        # 2. Reverese 2nd list
        current = slow.next
        prev = None
        next_ref = None
        while current:
            next_ref = current.next
            current.next = prev
            prev = current
            current = next_ref
        slow.next = None # last elem(tail node) of first list would point to None
        # 3. Merge two lists
        head1 = head
        head2 = prev #2nd list (reversed)
        while head2:
            # store next pointers before moving it forward
            next1 = head1.next
            next2 = head2.next
            # do merge
            head1.next = head2
            head2.next = next1
            # move forward
            head1 = next1
            head2 = next2
#time comp: O(n), process of finding the middle takes O(n/2),
                  #reversing the second half takes O(n/2),
                  #and merging also takes O(n/2), all of which sum up to O(n)
#space comp: O(1), in-place merging, no need for extra space
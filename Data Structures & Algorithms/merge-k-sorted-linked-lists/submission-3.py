# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Approach mentally:
# L0   L1   L2   L3   L4   L5   L6   L7
#  \___/     \___/     \___/     \___/
#    ↓         ↓         ↓         ↓

#    A         B         C         D
#     \_______/           \_______/
#         ↓                   ↓

#         X                   Y
#          \_________________/
#                   ↓
#                result

# Approach:
# 1) Create a helper function to merge 2 sorted linked lists.
# 2) Instead of merging lists one by one, merge them in pairs.
# 3) First merge lists 1 position apart, then 2 positions apart,
#    then 4 positions apart, and so on.
# 4) Keep doubling the merge distance until all lists are merged into lists[0].

# Time comp: O(N log k)
# N = total number of nodes across all k lists
# k = number of linked lists
# Space comp: O(1) auxiliary space
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: no lists
        if not lists:
            return None

        k = len(lists)

        # Distance between 2 lists/groups we want to merge
        interval = 1

        # Keep merging until interval becomes >= number of lists
        while interval < k:
            # Merge pairs:
                # interval = 1 -> (0,1), (2,3), (4,5)...
                # interval = 2 -> (0,2), (4,6)...
                # interval = 4 -> (0,4)...
            for i in range(0, k - interval, interval * 2):

                lists[i] = self.mergeTwo(
                    lists[i],
                    lists[i + interval]
                )

            # After each round, each merged group becomes twice as large
            interval *= 2

        # Fully merged list will be stored at index 0
        return lists[0]

    # Helper function to merge 2 sorted lists
    def mergeTwo(self, l1, l2) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next #always update current
        #attach remaining nodes to current
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next
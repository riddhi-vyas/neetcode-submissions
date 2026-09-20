## Approach:
#1. Insert copy nodes in-between original nodes
#2. Connect Random pointers
#3. Connect Next pointers
# Time comp: O(N)+O(N)+O(N)= O(3N) ~ O(N)
# Space comp: O(1), new copied nodes themselves don't count as aux space because they are the required output.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        #Step1 - create copied nodes for original -> place in-between original
        temp = head
        while temp:
            copy_node = Node(temp.val)
            copy_node.next = temp.next # Preserve the next original node
            temp.next = copy_node # Insert the copy after temp
            temp = copy_node.next # Move to the next original node
        
        #Step2 - Connect random pointers for copied nodes
        temp = head
        while temp:
            copy_node = temp.next
            #check if original's random is None or not
                #if None, copy_node's random will point to None
                #if not None,it's pointing to a node -> copy.random = original.random
            if not temp.random: #means original.random is None
                copy_node.random = None
            else:
                copy_node.random = temp.random.next #Because, temp.random's next = copy_node and I need to connect pointers of copied nodes
            temp = temp.next.next #always update temp after each iteration
        #Step3 - Connect next pointers for copied nodes
        dummy = Node(-1)
        temp = head
        copied_head = dummy
        while temp:
            copied_head.next = temp.next
            temp.next = temp.next.next
            copied_head = copied_head.next #update copied_head ptr
            temp = temp.next #update temp ptr
        return dummy.next
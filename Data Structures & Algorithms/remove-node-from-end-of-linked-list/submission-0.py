# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        og_head = head
        len_list = 0
        while head:
            len_list += 1
            head = head.next

        removal_index = len_list - n

        # ADDED: handle removing the head node
        if removal_index == 0:
            return og_head.next

        # ADDED: reset head since it's currently None
        head = og_head

        i = 0
        prev = None

        # CHANGED: use removal_index instead of n
        while i < removal_index and head:
            prev = head
            head = head.next

            # ADDED: increment i
            i += 1

        prev.next = head.next if head else None
        return og_head

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
			  # need to keep track of original head  
        og_head = head
        # calculate length of list
        len_list = 0
        while head:
            len_list += 1
            head = head.next

				# the index of removal will be the length of the list minus input value 'n'
        removal_index = len_list - n

        # edge case: removal_index is the head, which lets us simply return next node
        if removal_index == 0:
            return og_head.next

        # reset head after earlier iteration
        head = og_head

				# index tracker to see when we get to node marked for removal
        i = 0
        # tracker to hold onto previously iterated over value
        prev = None

        # iterate until i hits removal_index or end of list
        while i < removal_index and head:
            prev = head
            head = head.next

            # increment i at each step
            i += 1

				# if current node exists, have previous node point to next
				# if current node DNE, have previous node point to None
        prev.next = head.next if head else None
        
        # return original head of input list with new updated order
        return og_head
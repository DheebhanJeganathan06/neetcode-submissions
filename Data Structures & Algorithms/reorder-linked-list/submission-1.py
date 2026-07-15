class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
		    # edge case; if list has <= 1 node, automatically return
        if not head or not head.next:
            return

				# we will split list into two halves
				# the first half will start at the original lift head
        h1_head = head

        # use Floyd's tortoise and hare algorithm to
        # find midpoint
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # the second half will start one after the midpoint node
        h2_head = slow.next
        # we close off the first half at the midpoint node
        # by having it point to None
        slow.next = None

        # We reverse the second half starting from h2_head
        curr = None
        while h2_head:
            next_h2_head = h2_head.next
            h2_head.next = curr
            curr = h2_head
            h2_head = next_h2_head
        h2_head = curr

        # We now merge the first half (normal) and second half (reversed)
        # based on the instruction logic
        while h1_head and h2_head:
            next_h1_head = h1_head.next
            next_h2_head = h2_head.next

            h1_head.next = h2_head
            h2_head.next = next_h1_head

            h1_head = next_h1_head
            h2_head = next_h2_head
            
        # no explicit return necessary since the instructions state that
        # the function is void
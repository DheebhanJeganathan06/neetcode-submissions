class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        h1_head = head

        # Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Start of second half
        h2_head = slow.next
        slow.next = None

        # Reverse second half
        curr = None
        while h2_head:
            next_h2_head = h2_head.next
            h2_head.next = curr
            curr = h2_head
            h2_head = next_h2_head

        h2_head = curr

        # Merge
        while h1_head and h2_head:
            next_h1_head = h1_head.next
            next_h2_head = h2_head.next

            h1_head.next = h2_head
            h2_head.next = next_h1_head

            h1_head = next_h1_head
            h2_head = next_h2_head
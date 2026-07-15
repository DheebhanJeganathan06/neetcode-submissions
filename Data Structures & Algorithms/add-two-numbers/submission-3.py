# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        new_list = ListNode()
        curr = new_list

        i = 0
        carry = 0
        res = 0
        while l1 and l2:
            curr_val = l1.val + l2.val + carry
            carry = 1 if curr_val >= 10 else 0
            # res += curr_val * (10 ** i)
            new_node = ListNode(curr_val % 10)
            curr.next = new_node
            curr = new_node
            i += 1
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_val = l1.val + carry
            carry = 1 if curr_val >= 10 else 0
            # res += curr_val * (10 ** i)
            new_node = ListNode(curr_val % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next
        while l2:
            curr_val = l2.val + carry
            carry = 1 if curr_val >= 10 else 0
            # res += curr_val * (10 ** i)
            new_node = ListNode(curr_val % 10)
            curr.next = new_node
            curr = new_node
            l2 = l2.next

        # res += (curr_val * (10 ** i)) if carry == 1 else 0
        if carry == 1:
            curr.next = ListNode(1)
        return new_list.next


        
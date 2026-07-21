# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_list = ListNode()
        curr = res_list

        while True:
            curr_min = sys.maxsize
            for curr_list in lists:
                if curr_list:
                    curr_min = min(curr_min, curr_list.val)
            if curr_min == sys.maxsize:
                return res_list.next
            for i, curr_list in enumerate(lists):
                if curr_list and curr_list.val == curr_min:
                    lists[i] = curr_list.next
                    break
            curr.next = ListNode(curr_min)
            curr = curr.next
        
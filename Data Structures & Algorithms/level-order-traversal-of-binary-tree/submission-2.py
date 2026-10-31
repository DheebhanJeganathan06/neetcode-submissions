# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        vals = [root.val]
        while queue:
            res.append(vals)
            vals = []
            new_queue = []
            for x in queue:
                if x.left:
                    new_queue.append(x.left)
                    vals.append(x.left.val)
                if x.right:
                    new_queue.append(x.right)
                    vals.append(x.right.val)
            queue = new_queue
        return res

            

            



        
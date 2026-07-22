# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.levelOrderHelper(0, root, res)
        return res

    def levelOrderHelper(self, level, root, res):
        if root:
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            level += 1
            self.levelOrderHelper(level, root.left, res)
            self.levelOrderHelper(level, root.right, res)
        

        
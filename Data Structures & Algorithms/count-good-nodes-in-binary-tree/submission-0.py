# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return count
        self.count = 0

        def iterate(curr, comp):
            if not curr:
                return
            if curr.val >= comp:
                self.count += 1
                iterate(curr.left, curr.val)
                iterate(curr.right, curr.val)
            else:
                iterate(curr.left, comp)
                iterate(curr.right, comp)

        iterate(root, -1 * sys.maxsize)
        return self.count
        
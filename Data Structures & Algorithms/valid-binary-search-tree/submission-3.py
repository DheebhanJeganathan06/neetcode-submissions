# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
		    # calls helper with initial infinite bounds, since root by
		    # itself is not bounded
        return self.valid(root, float("-inf"), float("inf"))
       
    def valid(self, node, left, right):
			  # if a leaf has been reached, propagate True back up to parents/ancestors
        if not node:
            return True
        # if the current node doesn't fall within its own bounds, propagate False
        if not (node.val > left and node.val < right):
            return False
        # if the current node is valid, do a recursive call on valid for its
        # left and right children, updating their limits accordingly
        return self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right)
        
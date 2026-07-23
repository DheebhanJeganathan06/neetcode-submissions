# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        return self.inOrderTraversal(root, k)

    def inOrderTraversal(self, root, k):
        if not root:
            return None

        if root.left:
            left = self.inOrderTraversal(root.left, k)
            if left is not None:
                return left

        self.count += 1
        if self.count == k:
            return root.val

        if root.right:
            right = self.inOrderTraversal(root.right, k)
            if right is not None:
                return right
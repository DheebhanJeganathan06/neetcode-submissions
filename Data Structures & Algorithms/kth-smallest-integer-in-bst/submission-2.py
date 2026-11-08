# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		    # class variable to track current node's index
        self.count = 0
        # call to recursive helper
        return self.inOrderTraversal(root, k)

    def inOrderTraversal(self, root, k):
        # if we've reached a leaf node, then either the input
        # was null or there aren't even 'k' elements in the tree;
        # either way, we return None
        if not root:
            return None

				# if a left node exists, propagate the call down
				# we start with left for L-V-R iteration order
        if root.left:
            left = self.inOrderTraversal(root.left, k)
            # if we've gotten a non-None value, then we reached the k-th value,
            # so we can propagate that value back to the root recursive call
            if left is not None:
                return left

				# for processing the current node, we first update count by 1
				# this is 1-indexed because we update before processing and starting
				# value of count is 0
        self.count += 1
	      # if we've reached the k-th element, propagate that value back up
	      # to the root recursive call
        if self.count == k:
            return root.val

				# same logic as root.left
        if root.right:
            right = self.inOrderTraversal(root.right, k)
            if right is not None:
                return right
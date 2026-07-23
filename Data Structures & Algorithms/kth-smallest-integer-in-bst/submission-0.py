# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodesList = []
        self.inOrderTraversal(root, nodesList)
        return nodesList[k - 1]



    
    def inOrderTraversal(self, root, nodesList):
        if not root:
            return
        if root.left:
            self.inOrderTraversal(root.left, nodesList)
        nodesList.append(root.val)
        if root.right:
            self.inOrderTraversal(root.right, nodesList)
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map values to their indices in inorder for O(1) lookups
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def helper(left, right):
            if left > right:
                return None

            # Next root value is always the next item in preorder traversal
            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            mid = inorder_idx_map[root_val]

            # Build left subtree first, then right subtree
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)
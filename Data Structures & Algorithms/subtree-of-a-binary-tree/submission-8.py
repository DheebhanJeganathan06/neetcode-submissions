class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
		    # in case where our recursive calls have gone down to a leaf,
		    # the corresponding node in subRoot must also be a leaf for
		    # it to be a valid subtree
        if not root:
            return not subRoot

				# we use a sameTree helper function to check if a current node's tree matches
				# the subRoot tree
        if self.sameTree(root, subRoot):
            return True

				# in case the current node's tree doesn't match the subRoot tree,
				# we check the same thing for current node's left subtree and
				# current node's right subtree
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
        
	  # check Same Tree problem for more notes on this implementation
    def sameTree(self, p, q):
        if not p or not q:
            return p == q
        return (
            p.val == q.val and
            self.sameTree(p.left, q.left) and
            self.sameTree(p.right, q.right)
        )
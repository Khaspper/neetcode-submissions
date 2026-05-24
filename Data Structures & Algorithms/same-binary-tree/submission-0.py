# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def inorder(root1, root2):
            if not self.same or (not root1 and not root2):
                return
            if (not root1 or not root2) or (root1.val != root2.val):
                self.same = False
                return
            inorder(root1.left, root2.left)
            inorder(root1.right, root2.right)

        inorder(p, q)
        return self.same
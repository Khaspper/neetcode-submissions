# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root, parent, left, right):
            if not root:
                return True
            if left == True and right == False:
                return root.val < parent.val
            if left == False and right == True:
                return root.val > parent.val
            return (inorder(root.left, root, True, False) 
            and inorder(root.right, root, False, True))
        return inorder(root, None, True, True)






        
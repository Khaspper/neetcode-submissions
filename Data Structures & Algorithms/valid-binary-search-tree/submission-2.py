# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        rootVal = root.val
        def inorderCheck(root, parent, isLeftSide):
            if not root:
                return True
            childrenIsValid = inorderCheck(root.left, root, True) and inorderCheck(root.right, root, False)
            if not childrenIsValid:
                return False
            if parent == None:
                return True
            if isLeftSide and root.val < rootVal and root.val < parent.val:
                return True
            if not isLeftSide and root.val > rootVal and root.val > parent.val:
                return True
            return False
        return inorderCheck(root, None, False)

            

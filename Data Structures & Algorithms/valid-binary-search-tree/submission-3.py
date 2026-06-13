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
        def inorderCheck(root, parent, leftChildren, leftSide):
            if not root:
                return True
            isValid = inorderCheck(root.left, root, leftChildren, True) and inorderCheck(root.right, root, leftChildren, False)
            if not isValid:
                return False

            if (leftChildren and root.val < rootVal) and (leftSide and root.val < parent.val) or (not leftSide and root.val > parent.val):
                    return True
            elif (not leftChildren and root.val > rootVal) and (leftSide and root.val < parent.val) or (not leftSide and root.val > parent.val):
                return True
            return False

        return inorderCheck(root.left, root, True, True) and inorderCheck(root.right, root, False, False)
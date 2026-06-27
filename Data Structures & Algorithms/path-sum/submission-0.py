# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root, total):
            if not root:
                return False
            total += root.val
            if not root.left and not root.right:
                if total == targetSum:
                    return True
            else:
                if root.left:
                    if pathSum(root.left, total): return True
                if root.right:
                    if pathSum(root.right, total): return True
            return False
        return pathSum(root, 0)
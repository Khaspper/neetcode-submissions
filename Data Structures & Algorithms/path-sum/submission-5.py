# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findSum(root, total):
            if not root:
                return False

            total += root.val
            if total == targetSum and (not root.left and not root.right):
                return True
            return findSum(root.left, total) or findSum(root.right, total)
        return findSum(root, 0)
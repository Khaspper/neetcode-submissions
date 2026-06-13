# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        def inorder(root):
            if not root:
                return 0
            leftMax = inorder(root.left)
            rightMax = inorder(root.right)
            total = leftMax + rightMax + root.val
            currMax = max(root.val, leftMax + root.val, rightMax + root.val, total)
            self.maxSum = max(self.maxSum, currMax)
            return max(root.val, leftMax + root.val, rightMax + root.val)
        inorder(root)
        return self.maxSum
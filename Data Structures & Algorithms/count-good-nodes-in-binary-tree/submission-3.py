# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def findGoodNodes(root, largestValue):
            if not root:
                return
            if root.val >= largestValue:
                self.res += 1
                largestValue = root.val
            findGoodNodes(root.left, largestValue)
            findGoodNodes(root.right, largestValue)


        self.res = 1
        findGoodNodes(root.left, root.val)
        findGoodNodes(root.right, root.val)

        return self.res
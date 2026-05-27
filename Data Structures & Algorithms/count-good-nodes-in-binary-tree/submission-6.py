from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        q = deque([[root, root.val]])
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr[0].val >= curr[1]:
                    self.res += 1
                if curr[0].left:
                    q.append([curr[0].left, max(curr[0].val, curr[1])])
                if curr[0].right:
                    q.append([curr[0].right, max(curr[0].val, curr[1])])

        return self.res


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while len(q) > 0:
            right = True
            for i in range(len(q)):
                curr = q.popleft()
                res.append(curr.val) if right == True else None
                right = False
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return res
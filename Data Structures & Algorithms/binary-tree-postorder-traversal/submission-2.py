# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack, res = [], []

        while curr or stack:
            if not curr:
                temp = stack.pop()
                if temp[1] == True:
                    # Do something
                    res.append(temp[0].val)
                else:
                    stack.append([temp[0], True])
                    curr = temp[0].right
            else:
                stack.append([curr, False])
                curr = curr.left
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        curr = root
        self.res = [-1]
        self.index = 0

        while curr or stack:
            if not curr:
                curr = stack.pop()
                self.res.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left

    def next(self) -> int:
        self.index += 1
        return self.res[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.res) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
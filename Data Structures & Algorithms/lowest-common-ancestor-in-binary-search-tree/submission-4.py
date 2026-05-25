# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.pParents = set()
        self.qParents = set()
        def findNodesParents(root, node, child, depth):
            if not root:
                return False
            if root.val == node.val:
                if child == "q":
                    self.qParents.add((root,depth))
                else:
                    self.pParents.add((root,depth))
                return True
            if (findNodesParents(root.left, node, child, depth + 1) or findNodesParents(root.right, node, child, depth + 1)):
                if child == "q":
                    self.qParents.add((root,depth))
                    return True
                else:
                    self.pParents.add((root,depth))
                    return True
            else:
                return False
        findNodesParents(root, p, 'p', 0)
        findNodesParents(root, q, 'q', 0)

        lca = None
        for p in self.pParents:
            if p in self.qParents:
                if lca == None or p[1] > lca[1]:
                    lca = p
        return lca[0]
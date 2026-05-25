# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.pParents = {}
        self.qParenets = {}
        def findNodesParents(root, node, child):
            print(f'root: {root.val}')
            if not root:
                print(f'not root')
                return False
            if root == node:
                print(f'found node')
                return True
            if (findNodesParents(root.left, node, child) or findNodesParents(root.right, node, child)):
                print(f'findNodesParents(root.left, node, child) or findNodesParents(root.right, node, child')
                if child == "q":
                    print(f'q')
                    self.qParents.add(root)
                else:
                    print(f'p')
                    self.pParents.add(root)
                return True
            else:
                print(f'Returning False')
                return False
        findNodesParents(root, p, 'p')
        findNodesParents(root, q, 'q')
        print(f'self.pParents: {self.pParents}')
        print(f'self.qParenets: {self.qParenets}')
        return root
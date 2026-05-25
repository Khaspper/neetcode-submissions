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
                print(f'not root\n\n')
                return False
            print(f'root: {root.val}')
            if root.val == node.val:
                print(f'found node\n\n')
                if child == "q":
                    print(f'adding {root.val} to q \n\n')
                    self.qParents.add((root,depth))
                else:
                    print(f'adding {root.val} to p\n\n')
                    self.pParents.add((root,depth))
                return True
            if (findNodesParents(root.left, node, child, depth + 1) or findNodesParents(root.right, node, child, depth + 1)):
                print(f'findNodesParents(root.left, node, child) or findNodesParents(root.right, node, child')
                if child == "q":
                    print(f'adding {root.val} to q \n\n')
                    self.qParents.add((root,depth))
                    return True
                else:
                    print(f'adding {root.val} to p\n\n')
                    self.pParents.add((root,depth))
                    return True
            else:
                print(f'Returning False\n\n')
                return False
        findNodesParents(root, p, 'p', 0)
        print('finding q')
        findNodesParents(root, q, 'q', 0)
        print(f'self.pParents: {self.pParents}')
        print(f'self.qParenets: {self.qParents}')

        pString = ''
        for p in self.pParents:
            pString += f'[{p[0].val}, {p[1]}] -> '
        qString = ''
        for q in self.qParents:
            qString += f'[{q[0].val}, {q[1]}] -> '
        print(f'pString: {pString}')
        print(f'qString: {qString}')

        lca = None
        for p in self.pParents:
            if p in self.qParents:
                print(f'p: [{p[0].val}, {p[1]}] in q')
                if lca == None or p[1] > lca[1]:
                    lca = p

        print(f'lca: [{lca[0].val}, {lca[1]}]')
        return lca[0]
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
        def findNodesParents(root, node, child):
            if not root:
                print(f'not root\n\n')
                return False
            print(f'root: {root.val}')
            if root.val == node.val:
                print(f'found node\n\n')
                if child == "q":
                    print(f'adding {root.val} to q \n\n')
                    self.qParents.add(root)
                else:
                    print(f'adding {root.val} to p\n\n')
                    self.pParents.add(root)
                return True
            if (findNodesParents(root.left, node, child) or findNodesParents(root.right, node, child)):
                print(f'findNodesParents(root.left, node, child) or findNodesParents(root.right, node, child')
                if child == "q":
                    print(f'adding {root.val} to q \n\n')
                    self.qParents.add(root)
                    return True
                else:
                    print(f'adding {root.val} to p\n\n')
                    self.pParents.add(root)
                    return True
            else:
                print(f'Returning False\n\n')
                return False
        findNodesParents(root, p, 'p')
        print('finding q')
        findNodesParents(root, q, 'q')
        print(f'self.pParents: {self.pParents}')
        print(f'self.qParenets: {self.qParents}')

        pString = ''
        for p in self.pParents:
            pString += f'{p.val} -> '
        qString = ''
        for q in self.qParents:
            qString += f'{q.val} -> '
        print(f'pString: {pString}')
        print(f'qString: {qString}')

        lca = None
        for p in self.pParents:
            if p in self.qParents:
                if lca == None:
                    lca = p
                else:
                    lca = lca if lca.val < p.val else p
        print(f'lca: {lca.val}')
        return lca
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        fridge = [(root, 1)]

        while len(fridge) != 0:
            node, depth = fridge.pop(0)
            if node.left == None and node.right == None:
                return depth

            if node.left != None:
                fridge.append((node.left, depth + 1))

            if node.right != None:
                fridge.append((node.right, depth + 1))
        

if __name__ == '__main__':
    sol = Solution()
    tree3  = TreeNode(3)
    tree9  = TreeNode(9)
    tree20 = TreeNode(20)
    tree15 = TreeNode(15)
    tree7  = TreeNode(7)
    tree20.left = tree15
    tree20.right = tree7
    tree3.left = tree9
    tree3.right = tree20

    print sol.minDepth(tree3)
    print "Example 2"
    tree1  = TreeNode(1)
    tree2  = TreeNode(2)
    tree3  = TreeNode(3)
    tree4  = TreeNode(4)
    tree5  = TreeNode(5)

    tree1.left = tree2
    tree1.right = tree3
    tree3.left = tree4
    tree3.right = tree5
    print sol.minDepth(tree1)

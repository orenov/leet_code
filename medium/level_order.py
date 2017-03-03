# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def traverse(self, root, depth):
        if root == None:
            return []
        return [(root.val, depth)] + self.traverse(root.left, depth + 1) + self.traverse(root.right, depth + 1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        l = sorted(self.traverse(root, 0), key = lambda s: s[1])
        result = [[]]
        current = 0
        for i in l:
            if i[1] != current:
                current += 1
                result.append([])
            result[current].append(i[0])
                
        return result

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

    print sol.levelOrder(tree3)
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
    print sol.levelOrder(tree1)





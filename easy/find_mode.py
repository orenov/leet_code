# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def collectElements(self, root):
        if root == None:
            return []
        else:
            return [root.val] + self.collectElements(root.left) + self.collectElements(root.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = self.collectElements(root)
        d = {}
        maximum = 0
        for i in result:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

            if maximum < d[i]:
                maximum = d[i]
        output = []
        for i in d:
            if d[i] == maximum:
                output.append(i)

        print output

if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(1)
    tree.left = None
    tree2 = TreeNode(2)
    tree2.left = None
    tree2.right = TreeNode(2)
    tree.right = tree2
    print sol.findMode(tree)
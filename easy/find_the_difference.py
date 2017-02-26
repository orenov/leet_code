import argparse

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i not in d:
                return i
            elif d[i] == 0:
                return i
            else:
                d[i] -= 1



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find The Difference.')
    parser.add_argument('x', type=str, help='our base string')
    parser.add_argument('y', type=str, help='string with suffling and adding additional character')

    args = parser.parse_args()
    sol = Solution()

    print sol.findTheDifference(args.x, args.y)        
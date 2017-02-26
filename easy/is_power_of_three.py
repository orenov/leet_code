import argparse

class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        return 1162261467 % n == 0 and n > 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if Integer is power of Three.')
    parser.add_argument('x', type=int, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.isPowerOfThree(args.x)
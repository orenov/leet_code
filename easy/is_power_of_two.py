import argparse

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 1:
                return False
            n /= 2

        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if Integer is power of Two.')
    parser.add_argument('x', type=int, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.isPowerOfTwo(args.x)
        
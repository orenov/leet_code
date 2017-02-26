import argparse

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        while num != 1:
            if num % 4 != 0:
                return False
            num /= 4

        return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if Integer is power of Four.')
    parser.add_argument('x', type=int, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.isPowerOfFour(args.x)
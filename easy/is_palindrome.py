import argparse

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reverse = 0
        while (x > reverse):
            reverse = x % 10 + 10 * reverse
            x /= 10

        return reverse == x or reverse/10 == x

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check is Number Palindrome')
    parser.add_argument('x', type=int, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.isPalindrome(args.x)
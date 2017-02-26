import argparse

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += n % 2
            n /= 2

        return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate Hamming Weight For 32-bit signed integer')
    parser.add_argument('x', type=int, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.hammingWeight(args.x)
        
import argparse

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        length = max(len(x), len(y))
        x = x.zfill(length)
        y = y.zfill(length)
        count = 0
        for i in xrange(0, len(x)):
            if x[i] != y[i]:
                count += 1

        return count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate Hamming Distance')
    parser.add_argument('x', type=int, help='first integer')
    parser.add_argument('y', type=int, help='second integer')

    args = parser.parse_args()
    sol = Solution()

    print sol.hammingDistance(args.x, args.y)


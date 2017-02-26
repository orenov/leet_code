import argparse

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int('0b' + '1' * (len(bin(num))-2), 2) ^ num
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find Complement Number which is reversed by bits.')
    parser.add_argument('x', type=int, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.findComplement(args.x)
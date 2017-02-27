import argparse

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        result = ""
        sign = ""
        if num < 0:
            sign = "-"
            num = abs(num)

        while num != 0:
            result = str(num % 7) + result
            num /= 7

        return sign + result
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert To Base 7.')
    parser.add_argument('x', type=int, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.convertToBase7(args.x)
import argparse

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #DCXXI
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        roman_ixc = {'I':5, 'X':50, 'C':500}       
        value = 0
        for i in reversed(s):
            if i in roman_ixc and value >= roman_ixc[i]:
                value -= roman_dict[i]
            else:
                value += roman_dict[i]
        return value
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Roman Number To Integer')
    parser.add_argument('x', type=str, help='roman number as string')

    args = parser.parse_args()
    sol = Solution()

    print sol.romanToInt(args.x)
        
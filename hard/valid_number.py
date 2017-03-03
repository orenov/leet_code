import argparse

class Solution(object):
    def validate(self, s, full = True):
        if len(s) == 0:
            return False
            
        if s[0] == '-' or s[0] == '+':
            s = s[1:]

        if s.isdigit():
            return True

        if full:
            s = s.replace('.','',1)
            if s.isdigit():
                return True

        return False

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip()
        
        if len(s) == 0:
            return False

        s = s.split('e')
        if len(s) == 2:
            return self.validate(s[0]) and self.validate(s[1], False)
        elif len(s) == 1:
            return self.validate(s[0])
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='String to check')
    parser.add_argument('x', type=str, help='our number')

    args = parser.parse_args()
    sol = Solution()

    print sol.isNumber(args.x)
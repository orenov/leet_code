import argparse

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if ord(word[0]) < 97:
            c1 = 0
            c2 = 0
            for i in xrange(1, len(word)):
                if ord(word[i]) < 97:
                    c1 += 1
                    if c2 != 0:
                        return False
                else:
                    c2 += 1
                    if c1 != 0:
                        return False
        else:
            for i in xrange(1, len(word)):
                if ord(word[i]) < 97:
                    return False

        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Detect Captital Usage.')
    parser.add_argument('x', type=str, help='string to check')

    args = parser.parse_args()
    sol = Solution()

    print sol.detectCapitalUse(args.x)     
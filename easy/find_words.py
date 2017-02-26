import argparse

class Solution(object):
    def __init__(self):
        self.line1 = 'qwertyyuiop'
        self.line2 = 'asdfghjkl'
        self.line3 = 'zxcvbnm'

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            c1 = 0
            c2 = 0
            c3 = 0
            valid = True
            for letter in word:
                if letter in self.line1:
                    c1 += 1
                    if c2 + c3 != 0:
                        valid = False
                        break
                elif letter in self.line2:
                    c2 += 1
                    if c1 + c3 != 0:
                        valid = False
                        break
                elif letter in self.line3:
                    c3 += 1
                    if c2 + c1 != 0:
                        valid = False
                        break
            if valid:
                result.append(word)
        return result

if __name__ == '__main__':
    sol = Solution()

    print sol.findWords(["hello", "Alaska", "Dad", "Peace"])   
class Solution(object):
    def calculateMask(self, word):
        mask = 0
        for c in word:
            mask |= (1 << (ord(c) - 97))
        return mask

    def maxProduct2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = map(lambda s: (len(s), self.calculateMask(s)), words)
        max_prod = 0
        for i in xrange(len(words)-1):
            for j in xrange(i, len(words)):
                if not words[i][1] & words[j][1] and words[i][0] * words[j][0] > max_prod:
                    max_prod = words[i][0] * words[j][0] 
        return max_prod

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert sol.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
    assert sol.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0
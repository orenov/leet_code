import argparse

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = [0] * len(nums)
        d = {0 : "Gold Medal", 1 : "Silver Medal", 2 : "Bronze Medal"}
        for i, x in enumerate(sorted(range(len(nums)), key = lambda y: -nums[y])):
            if i in d:
                output[x] = d[i]
            else:
                output[x] = str(i+1)
        return output

if __name__ == '__main__':
    sol = Solution()
    l = [10,3,8,9,4]
    print l
    print sol.findRelativeRanks(l)   
    #output ["Silver Medal", "Gold Medal", "Bronze Medal", "4", "5"]
    #[(4, 1), (3, 2), (2, 3), (1, 4), (0, 5)]
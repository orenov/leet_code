class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(0, len(nums)):
            s = target - nums[i]
            if s in d:
                return [d[s], i] 
            d[nums[i]] = i
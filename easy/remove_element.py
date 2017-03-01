class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in xrange(0, len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
        
if __name__ == '__main__':
    sol = Solution()
    print sol.removeElement([], 1)
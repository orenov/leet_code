class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        count = 0
        for i in xrange(len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1

        if count == 0:
            count += 1

        return count


if __name__ == '__main__':
    sol = Solution()
    print sol.removeDuplicates([1,1])
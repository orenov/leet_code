class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = set()
        sum = 0
        for number in nums:
            sum ^= number
            if number in d:
                sum -= number
                d.remove(number)
            else:
                sum += number
                d.add(number)

        return sum

    def singleNumber2(self, nums):
        sum = 0
        for number in nums:
            sum ^= number
        return sum

    def singleNumber3(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)
        
if __name__ == '__main__':
    sol = Solution()
    print sol.singleNumber([1,1,2,2,2,2,3])
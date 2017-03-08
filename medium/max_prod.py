class Solution(object):
    def maxProduct(self, nums):
        maxim = big = small = nums[0]
        for i in nums[1:]:
            l_big = max(n, n*big, n*small)
            l_small = min(n, n*big, n*small)
            big = l_big
            small = l_small
            maxim = max(maxim,big)
        return maxim

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProduct([2,3,-2,4,8])
    print sol.maxProduct([-2])
    print sol.maxProduct([0,2])
    print sol.maxProduct([-2,3,-4])
    print sol.maxProduct([-4,-3,-2])
    print sol.maxProduct([-3,0,1,-2])
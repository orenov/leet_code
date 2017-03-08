class Solution(object):
    '''
        - Possible imporvements: switch to binary search
    '''
    def insertInSortedArray(self, arr, elem):
        if arr[-1] > elem:
            return arr
        for i in xrange(len(arr)):
            if elem > arr[i]:
                arr[i:i] = [elem]
                del arr[-1]
                break
        return arr

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = sorted(nums[:k], key=lambda s: -s)
        for i in xrange(k, len(nums)):
            result = self.insertInSortedArray(result, nums[i])
        return result[k-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.findKthLargest([3,11,2,1,5,6,4], 2)
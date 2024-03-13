class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while True:
            mid = l + ((r - l) // 2)
            if nums[mid-1] >= nums[mid]:    # mid = 0, mid = -1 (last)
                return nums[mid]
            else:
                if nums[r] > nums[mid]:     # in the right partition
                    r = mid-1
                else:
                    l = mid+1
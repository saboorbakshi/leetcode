class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            else:
                # left sorted portion
                if nums[mid] > nums[r]:
                    # move right
                    if target > nums[mid] or target < nums[l]:
                        l = mid+1
                    else:
                        r = mid-1
                # right sorted portion
                else:
                    # move left
                    if target < nums[mid] or target > nums[r]:
                        r = mid-1
                    else:
                        l = mid+1
        return -1
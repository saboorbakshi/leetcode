class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumBetter(self, nums, target):
      hashmap = {}                             # dict basically
      for i, num in enumerate(nums):
          complement = target - num
          if complement in hashmap:
              return [i, hashmap[complement]]
          else:
              hashmap[num] = i 

Solution().twoSum([3, 2, 4], 6)
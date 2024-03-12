from typing import List

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()

        for n in nums:
            s.add(n)
        
        if len(s) == len(nums):
            return False
        else:
            return True

nums = [1, 1, 2, 3]
print(Solution().containsDuplicate(nums))
from typing import List

class Solution:

    '''
    insert each item in a set until you come across a previously inserted element
    time: O(n)
    space: O(n)
    '''

    def containsDuplicate1(self, nums: List[int]) -> bool:
 
        # :type nums: List[int]
        # :rtype: bool
        
        s = set()
        
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False

        
        
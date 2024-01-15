from typing import List

class Solution:
    '''
    iterate through the list, for each num, compute diff needed to get target
    if diff in hashmap, indicies found, else add the num to the hashmap
    time: O(n)
    space: O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return (hashMap[diff], i)
            else:
                hashMap[num] = i
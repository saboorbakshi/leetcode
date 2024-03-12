class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        sorted_tuple_list = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        return [tup[0] for tup in sorted_tuple_list[:k]]
    

    def topKFrequentBetter(self, nums, k):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums))]
        for num, count in counts.items():
            freq[count-1].append(num)
        
        ret = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret


"""
hashmap[n] = hashmap.get(n, 0) + 1

OR

if n in hashmap:        
  hashmap[n] += 1            
else:
  hashmap[n] = 1
"""
                
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s = set()
        sorted_strs = []
        for str in strs:
            sorted_str = ''.join(sorted(str))
            sorted_strs.append(sorted_str)
            s.add(sorted_str)
        
        ans = {}
        for str in s:
            ans[str] = []
        for i, str in enumerate(strs):
            ans[sorted_strs[i]].append(str)
        return list(ans.values())
    

    def groupAnagramsBetter(self, strs):
        ans = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in ans:
                ans[sorted_str] = [str]
            else:
                ans[sorted_str].append(str)
        return list(ans.values())
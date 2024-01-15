from array import array

class Solution:
    '''
    find the character frequencies for each string and check if they match
    time: O(n+m)
    space: O(n+m)
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS, dictT = {}, {}

        for c in s:
            dictS[c] = dictS.get(c, 0) + 1   # if key does not exist, it creates it with value 0
        for c in t:
            dictT[c] = dictT.get(c, 0) + 1

        return dictS == dictT
    
    '''
    get the unique set of characters in s, check if each character's frequency matches in s and t
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        unique = set(s)

        for c in unique:
            if s.count(c) != t.count(c):
                return False
        return True

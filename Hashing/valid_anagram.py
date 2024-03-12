class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k = set()

        k.add(''.join(sorted(s)))
        k.add(''.join(sorted(t)))

        if len(k) == 1:
            return True
        else:
            return False
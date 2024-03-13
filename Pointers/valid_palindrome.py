class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = ''
        for c in s:
            if c.isalnum():
                if c.isdigit():
                    new += c
                else:
                    new += c.lower()
        return new == new[::-1]
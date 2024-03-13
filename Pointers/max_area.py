class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = max(area, w * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
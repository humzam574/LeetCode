class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxv = 0
        left = 0
        right = len(height)-1
        while (left < right):
            if height[left] < height[right]:
                if height[left]*(right-left) > maxv:
                    maxv = height[left] * (right-left)
                left+=1
            elif height[left] >= height[right]:
                if height[right]*(right-left) > maxv:
                    maxv = height[right]*(right-left)
                right-=1
        return maxv
        

        
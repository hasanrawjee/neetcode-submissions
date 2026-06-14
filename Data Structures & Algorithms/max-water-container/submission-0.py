class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        mostWater = 0

        while l < r:
            waterArea = (r-l) * min(heights[r], heights[l])
            mostWater = max(mostWater, waterArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mostWater

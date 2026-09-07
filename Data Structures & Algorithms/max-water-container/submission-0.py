class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res, m = 0, 0

        while l < r:
            res = min(heights[l], heights[r]) * (r - l)
            m = max(res, m)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            

        return m
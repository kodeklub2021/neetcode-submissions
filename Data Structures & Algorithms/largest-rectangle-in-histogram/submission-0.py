class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxSum = 0
        l,r = 0,0
        cache = [0]* len(heights)

        for l in range(len(heights)):
            r = l
            while r < len(heights):
                curr = (r - l + 1) * min(heights[l:r+1])
                maxSum = max(maxSum, curr)
                print(f'l = {l} , r = {r} , curr = {curr} , maxSum = {maxSum}')
                r += 1
        return maxSum


        
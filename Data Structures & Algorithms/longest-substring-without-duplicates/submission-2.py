class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        cache = []
        maxL = 0

        for r in range(len(s)):
            while s[r] in cache:
                cache = cache[1:]
                l += 1
            cache.append(s[r])
            maxL = max(maxL, r-l+1)
        return maxL
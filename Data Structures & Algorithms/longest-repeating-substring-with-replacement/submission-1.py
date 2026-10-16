class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        cache = {}
        maxCount = 0
        maxFreq = 0

        l,r = 0,0

        for r in range(len(s)):

            cache[s[r]] = cache.get(s[r],0) + 1
            maxFreq = max(maxFreq, cache[s[r]])

            while r-l+1 - maxFreq > k:
                cache[s[l]] -= 1
                l += 1

            maxCount = max(maxCount, r-l+1)
        return maxCount
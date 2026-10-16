class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}

        for s in strs:
            x = ''.join(sorted(s))
            if x in cache:
                cache[x].append(s)
            else:
                cache[x] = [s]
        return [cache[i] for i in cache ]
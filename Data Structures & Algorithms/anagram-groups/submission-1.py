class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            order = ''.join(sorted(s))
            if order in hash:
                hash[order].append(s)
            else:
                hash[order] = [s]

        return [i for i in hash.values()]
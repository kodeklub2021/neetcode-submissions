class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        sorted_hash = sorted(hash.items(), key = lambda item: item[1],reverse=True)[:k]
        return [i[0] for i in sorted_hash]
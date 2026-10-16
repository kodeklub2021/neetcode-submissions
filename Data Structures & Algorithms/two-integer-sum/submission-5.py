class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,n in enumerate(nums):
            if target - n in hash:
                return sorted([i,hash[target-n]])
            else:
                hash[n]=i
        return []
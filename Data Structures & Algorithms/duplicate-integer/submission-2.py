class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = {}
        for n in nums:
            if n in set:
                return True
            else:
                set[n] = 1
        return False

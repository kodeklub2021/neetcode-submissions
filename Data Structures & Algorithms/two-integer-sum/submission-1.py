class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for n in range (len(nums)):
            x = target - nums[n]
            if x in cache:
                print('found target')
                return [cache[x],n]
            else:
                cache[nums[n]] = n
            print(f'cache = {cache}')
        return []

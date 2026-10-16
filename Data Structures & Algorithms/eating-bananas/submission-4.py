class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        ans = r

        while l<r:
            mid = (r+l)//2
            temp = [math.ceil(x/mid) for x in piles]
            curr = sum(temp)
            print(f'temp = {temp} , sum = {curr}, mid = {mid}')

            if curr <= h:
                ans = min(ans,mid)
                r = mid
            else:
                l = mid + 1


        return ans


        
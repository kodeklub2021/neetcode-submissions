from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k == 1 : return nums

        ans = []
        q = deque()

        l,r = 0,0

        while r < len(nums):
            print(f'curr = {nums[r]} , l = {l} ,  r = {r}', end =' ')

            while q and q[-1] < nums[r]:
                x = q.pop()
                print(f'popped {x} from deque', end =' ')
                # r += 1
            q.append(nums[r])
            print(f'deque = {q}')

            if (r-l+1) >= k:    
                ans.append(q[0])
                print(f'ans = {ans}')
                if nums[l] == q[0]:
                    popped = q.popleft()
                    print(f'removed {popped} from deque as it is going out of window', end =' ')
                l += 1
                 
            r += 1

        return ans




        
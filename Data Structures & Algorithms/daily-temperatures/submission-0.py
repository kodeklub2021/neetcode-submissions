from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        q = []

        for i,t in enumerate(temperatures):
            print(f'i = {i} and t = {t}')
            while q and q[-1][1] < t:
                popI, popT = q.pop()
                # print(popI,popT)
                if popT < t:
                    ans[popI] = i - popI

            q.append([i,t])
            print(f'q = {q}, ans = {ans}')
        return ans
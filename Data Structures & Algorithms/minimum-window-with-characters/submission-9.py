from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): return ""
        elif len(s) == len(t) and sorted(s) != sorted(t) : return ""

        need = Counter(t)
        have = Counter()
        needL = len(need)
        haveL = 0
        l = 0
        ans = [-1,-1]
        ansL = float("inf")

        for r in range(len(s)):

            curr = s[r]
            have[curr] = have.get(curr,0) + 1
            print(s[l:r+1],"  --  ", "have == ",have)
                
            if curr in need and have[curr] == need[curr] :
                haveL += 1
                print(f"enough {curr} present")

            while haveL == needL:
                print(f"current string = {s[l:r+1]} , l = {l} , r = {r}")
                if r-l+1 < ansL:
                    ansL = min(r-l+1, ansL)
                    ans = [l,r]
                    print("curr ans = ",s[l:r+1], " haveL = ",haveL, " ans = ",ans, "ansL = ",ansL)
                else:
                    print("we have need but its big = ",s[l:r+1], " haveL = ",haveL, " ans = ",ans, "ansL = ",ansL)

                temp = s[l]
                if temp in need:
                    have[temp] -= 1
                    if have[temp] < need[temp]:
                        haveL -= 1

                l += 1


                        

           


        l,r = ans
        return s[l:r+1]
        
                
                


            

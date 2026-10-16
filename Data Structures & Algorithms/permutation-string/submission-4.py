from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        need = Counter(s1)
        l1 = len(s1)

        if len(s1) > len(s2):
            return False
        
        window = Counter()
        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1
            print('window = ',window)

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                l += 1
                print('window = ',window)


            if window == need:
                print('match = ',window)
                return True

        return False



        


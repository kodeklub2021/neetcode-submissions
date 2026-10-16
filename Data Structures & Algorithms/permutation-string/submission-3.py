class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l,r = 0,len(s1)
        s1 = ''.join(sorted(s1))
        while r < len(s2)+1:
            curr = (s2[l:r])
            curr = ''.join(sorted(curr))
            if curr == s1:
                return True
            else:
                l+=1
                r+=1
            print("frame = ",curr," and s1 = ",s1)
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq1 = {}
        # for char1 in s1:
        #     freq1[char1] = freq1.get(char1,0) + 1

        l,r = 0,len(s1)
        s1 = ''.join(sorted(s1))
        while r < len(s2)+1:
            curr = ([x for x in s2[l:r]])
            curr = ''.join(sorted(curr))
            if curr == s1:
                return True
            else:
                l+=1
                r+=1
            print("frame = ",curr," and s1 = ",s1)
        return False


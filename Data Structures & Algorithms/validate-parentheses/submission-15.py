class Solution:
    def isValid(self, s: str) -> bool:
        hash = [s[0]]
        
        for i in s[1:]:
            if len(hash) == 0 and i in ["]","}",")"] : return False
            if (i == "]" and hash[-1] == "["
                or i == ")" and hash[-1] == "("
                or i == "}" and hash[-1] == "{"):
                hash = hash[:-1]
            else:
                hash.append(i)
        return len(hash) == 0
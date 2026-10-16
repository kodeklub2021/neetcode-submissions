from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Prefix each string with its length and a special marker
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the separator
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # get length of the string
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for st in strs:
            print(st)
            for s in st:
                enc += str(ord(s)+5)
                enc += " "
            enc+="##"
        print('encoded = ',enc)
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        words = s.split('##')[:-1]
        print('words = ',words)
        for word in words:
            temp = ""
            letters = word.split(' ')
            for l in letters:
                if l == '':
                    pass
                else:
                    temp += chr(int(l)-5)
            dec.append(temp)
        return dec

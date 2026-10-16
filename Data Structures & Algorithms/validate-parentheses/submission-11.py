from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        ans = deque()

        for char in s:
            print(f'curr char is {char}  --  ', end = ' ')
            if char in ["(" , "[" , "{"]:
                # print(f'{ans} -- adding char = {char}')
                ans.append(char)
            elif ans:
                if char == ")" and ans[-1] == "(":
                    ans.pop()
                elif char == "]":
                    if ans[-1] == "[":
                        ans.pop()
                    else:
                        ans.append(char)
                elif char == "}" :
                    if ans[-1] == "{":
                        ans.pop()
                    else:
                        ans.append(char)

                # print(f'{ans} -- popping char = {char}')
                
            else:
                ans.append(char)
                # print(f'{ans} -- adding char = {char}')

            print(f'queue = {ans}')

        return len(ans) == 0
                
        
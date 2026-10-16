from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()
        ans = 0
        for t in tokens:
            if t in "+-*/":
                
                a = q.pop()
                b = q.pop()
                print(f'a = {a}, b = {b}')

                if t == "+":
                    q.append(a+b)
                elif t == "-":
                    q.append(b-a)
                elif t == "*":
                    q.append(a*b)
                elif t == "/":
                    q.append(int(b/a))
                print(f'q = {q}')
            else:
                q.append(int(t))
            print(f'q = {q}')
        return q[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1 and tokens[0] not in "+-*/":
            return int(tokens[0])
        stack = []
        ops = ['+','-','*','/']
        for t in tokens:
            if t in ops:
                if stack:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    if t == "+":
                        stack.append(a + b)
                    elif t == "-":
                        stack.append(a - b)
                    elif t == "*":
                        stack.append(a * b)
                    elif t == "/":
                        stack.append(int(a / b))
            else:
                stack.append(t)
        if stack:
            return stack[-1]

        
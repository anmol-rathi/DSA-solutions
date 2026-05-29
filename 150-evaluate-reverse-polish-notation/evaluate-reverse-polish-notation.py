class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                a1=stack.pop()
                b1=stack.pop()
                if(i=="+"):
                    c=a1+b1
                elif(i=="-"):
                    c=b1-a1
                elif(i=="*"):
                    c=a1*b1
                else:
                    c=int(b1/a1)
                stack.append(c)
        return stack[-1]

        
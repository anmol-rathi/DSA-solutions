class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        count=0
        if k==len(num):
            return '0'
        for i in range(len(num)):
            if not stack:
                stack.append(num[i])
            elif stack[-1]<=num[i] or k==0:
                stack.append(num[i])
            else:
                while(stack and stack[-1]>num[i]) and k!=0:
                    stack.pop()
                    k-=1
                stack.append(num[i])
          
        while k!=0:
            stack.pop()
            k-=1
        
        while stack and stack[0]=='0':
            stack.pop(0)
        if not stack:
            return '0' 
        return ''.join(stack)
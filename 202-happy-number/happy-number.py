class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        print(n%10)
        s.add(n)
        while(True):
            temp=0
            while(n):
                temp+=(n%10)**2
                n-=n%10
                n=n/10
            print(temp)
            if temp==1:
                return True
            elif temp in s:
                return False
            else:
                s.add(temp)
            n=temp
                

          
            
        
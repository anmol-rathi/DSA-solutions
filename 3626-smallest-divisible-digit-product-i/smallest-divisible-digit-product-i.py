class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # n=100
        # a=n%10
        # n=n//10
        # c=n%10
        # n=n//10
        
        a=n%10
        # n=n//10
        
        print(10%2)

        while True:
            if n<10:
                a=n%10
                if a%t==0:
                    return n
            elif n>9 and n<100:
                a=n%10
                b=n//10%10
                if (a*b)%t==0:
                    return n
            else:
                a=n%10
                b=n//10%10
                c=n//100%10
                if (a*b*b)%t==0:
                    return n
            n+=1
                


        
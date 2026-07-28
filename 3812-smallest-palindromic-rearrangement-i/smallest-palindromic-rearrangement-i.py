class Solution:
    def smallestPalindrome(self, s: str) -> str:
        q=len(s)
        a=''
        b=''
        if len(s)%2==0:
            # b=(q/2)-1
            # print(b)
            a+=s[0:int(q/2):1]
            a=sorted(a)
            b=a[::-1]
            c=''.join(b)
            d=''.join(a)+c
            return(d)
            # print(d)
        if len(s)%2!=0:
            a+=s[0:int(q/2):1]
            a=sorted(a)
            b=a[::-1]
            c=''.join(b)
            d=''.join(a)+s[int(len(s)/2)]+c
            return(d)
            # print(d)



        

            
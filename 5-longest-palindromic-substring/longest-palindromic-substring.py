class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=''
        for i in range(n):
            a=b=i
            while a>=0 and b<n and s[a]==s[b]:
                a-=1
                b+=1
            temp=s[a+1:b]
            # print(temp)
            if len(temp)>len(ans):
                ans=temp

            a,b=i,i+1
            while a>=0 and b<n and s[a]==s[b]:
                a-=1
                b+=1
            temp=s[a+1:b]
            if len(temp)>len(ans):
                ans=temp
        
        return ans

            
        
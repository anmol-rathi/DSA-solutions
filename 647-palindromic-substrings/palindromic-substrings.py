class Solution:
    def countSubstrings(self, s: str) -> int:
        # res=[]
        count=0
        n=len(s)
        for i in range(n):
            a=b=i
            while a>=0 and b<n and s[a]==s[b]:
                # res.append(s[a:b+1])
                count+=1
                a-=1
                b+=1
            a,b=i,i+1
            while a>=0 and b<n and s[a]==s[b]:
                # res.append(s[a:b+1])
                count+=1
                a-=1
                b+=1
        return count
        
        

        
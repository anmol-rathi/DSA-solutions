class Solution:
    def minimumPushes(self, word: str) -> int:
        a=len(word)
        d=1
        res=0
        q=0
        count=Counter(word)
        print(count)
        heap=[]
        for s,freq in count.items():
            heapq.heappush(heap,(-freq,s))
        while(heap):
            if q==8 or q==16 or q==24:
                d+=1
            f,ch=heapq.heappop(heap)
            res+=d*(-f)
            q+=1
            print(heap)
            print(res)
            print(q)
        return res
       

        
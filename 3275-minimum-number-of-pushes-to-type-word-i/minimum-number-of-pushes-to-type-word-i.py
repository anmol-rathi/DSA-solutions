class Solution:
    def minimumPushes(self, word: str) -> int:
        a=len(word)
        # b=a%8
        # print(b)
        # print(a)
        d=1
        res=0
        while (a>0):
            # print('hello')
            if (a/8 <1):
                res=res+((a%8)*d)
                # print(res)
                # print(a%8)
                a=-8
                # print('hi')
            else:
                res=res+(8*d)
                # print(res)
                d+=1
                a-=8
                # print(a)
        print(res)
        return res
        #         c=a/8
        #         res=c*d
        # c=int(a/8)
        # print(c)
        # res=c*d*8
        # print(res)

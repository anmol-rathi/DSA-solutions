class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        # a,b=intervals[0]
        arr=[]
        arr.append(intervals[0])
        n=len(intervals)
        if n==1:
            return intervals
        count=1
        while count<n:
            a,b=arr.pop()
            p,q=intervals[count]
            if b>=p:
                if b>=q:
                    arr.append([a,b])
                else:
                    arr.append([a,q])
            else:
                arr.append([a,b])
                arr.append([p,q])
            count+=1
        # print(arr)
        return arr

        
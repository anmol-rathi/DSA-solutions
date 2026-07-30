class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        arr=[]
        arr.append(intervals[0])
        count=1
        while(count<n):
            a,b=arr.pop()
            p,q=intervals[count]
            if b<=p:
                arr.append([a,b])
                arr.append([p,q])
            else:
                if b>=q:
                    arr.append([p,q])
                else:
                    arr.append([a,b])
            count+=1
        # print(arr)
        return len(intervals)-len(arr)
        
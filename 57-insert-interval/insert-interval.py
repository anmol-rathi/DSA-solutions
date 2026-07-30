class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        stack=[]
        # print(intervals)
        intervals.sort()
        n=len(intervals)
        # print(intervals)
        # =intervals[0]
        arr=[]
        arr.append(intervals[0])
        # print(p,q)
        count=1
        while count<n:
        # for i in range(1,n)
            a,b=intervals[count]
            p,q=arr.pop()
            if q>=a:
                if q>=b:
                    arr.append([p,q])
                    
                else:
                    arr.append([p,b])
            else:
                arr.append([p,q])
                arr.append([a,b])
            count+=1
        # print(arr)
        return arr


            
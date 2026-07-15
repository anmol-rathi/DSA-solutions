class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=2
        odd=1
        if n==0:
            return 0
        for i in range(1,n):
            odd= odd + 1+ 2*i
            even= even+ 2+ 2*i
        print(odd,even)
        return gcd(odd,even)
        # i=0
        # j=0
        # while(i < n )
        
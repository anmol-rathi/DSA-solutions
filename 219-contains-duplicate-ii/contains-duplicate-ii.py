class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sw=set()
        for i,num in enumerate(nums):
            if num in sw:
                return True
            sw.add(num)
            if(len(sw)>k):
                sw.remove(nums[i-k])
        return False
        
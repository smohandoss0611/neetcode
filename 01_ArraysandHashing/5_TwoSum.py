from typing import List
class Solution:
    def twoSums(self, nums: List[int],target: int) -> int:
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n 
            if diff in hashmap:
               return(hashmap[diff],i)
            hashmap[n] = i

s = Solution()
nums =[1,3,4,5,2]
target = 7
result = s.twoSums(nums,target)
print(result)
            


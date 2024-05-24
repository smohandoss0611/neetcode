from typing import List
class Solution:
    def removeelements(self, nums: List[int],val: int) -> int:
        l  = 0
        for r in range(len(nums)):
            if nums[r] != val:
              nums[l] = nums[r]
              l = l +1
        return l
    
s= Solution()
nums = [1,2,3,55,55,3]
result = s.removeelements(nums,2)
print(result)
print(nums[:result])

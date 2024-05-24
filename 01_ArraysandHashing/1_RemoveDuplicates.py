from typing import List
class Solution:
    def findduplicate(self,nums : List[int]) -> int:
        l = 0
        for r in range(0,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
s= Solution()
nums = [0,0,1,1,2,2,2,3,3,4,5]
result = s.findduplicate(nums)
print(result)
print(nums[:result])
    



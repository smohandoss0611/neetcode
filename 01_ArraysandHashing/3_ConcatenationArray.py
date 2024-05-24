from typing import  List
class Solution:
    def concatenationlist(self,nums: List[int]) -> int:
        ans =[]
        for i in range(2):
          for n in nums:
              ans.append(n)
        return ans
    
s = Solution()
nums =[1,2,3]
result = s.concatenationlist(nums)
print(result)
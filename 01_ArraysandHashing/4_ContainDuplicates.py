from typing import List

class Solution:
    def containDuplicates(self,nums : List[int]) -> bool :
        hashset = set()
        for n in nums:
            if n in hashset:
               return True
            hashset.add(n)
        return False
s  = Solution()
nums =[11,33,34,33]
result = s.containDuplicates(nums)
print(result)

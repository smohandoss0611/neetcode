from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

s = Solution()
print(s.hasDuplicate([1,2,3,8,4,4,5]))


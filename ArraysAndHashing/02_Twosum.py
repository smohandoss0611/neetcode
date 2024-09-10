from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map ={}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in complement_map and complement_map[complement] != i:
                return[complement_map[complement],i]
            complement_map[n] = i

s = Solution()
print(s.twoSum([2,7,11,16],9))
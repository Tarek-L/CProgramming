class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            x = target - nums[i]
            if x in s:
                return [s[x],i]
            
            s[nums[i]] = i
        

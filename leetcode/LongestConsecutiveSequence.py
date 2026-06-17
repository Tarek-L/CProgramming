class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1

        l = sorted(list(set(nums)))
        currLength = 1
        maxLength = 1

        for i in range(1,len(l)):
            if l[i] - l[i-1] == 1: currLength += 1
            else:
                currLength = 1
            maxLength = max(maxLength, currLength)
        return maxLength

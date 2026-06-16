class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#        res = [0]*len(nums)
#        p = 1
#        z = False
#        dz = False
#        for i in nums:
#            if i != 0:
#                p *= i
#            elif i == 0 and z:
#                dz = True
#            else:
#                z = True
#        if z:
#            if dz:
#                return res
#            for i in range(len(nums)):
#                if nums[i] == 0:
#                    res[i] = p
#            return res
#        else:
#            for i in range(len(nums)):
#                res[i] = p // nums[i]
#            return res
        res = [1]*len(nums)
        for i in range(len(res)-2,-1,-1):
            res[i] = nums[i+1] * res[i+1] 
        suffix = nums[0]
        for i in range(1,len(res)):
            res[i] *= suffix
            suffix *= nums[i]
        return res





        

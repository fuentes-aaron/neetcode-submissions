class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero +=1
                continue
            total = total*num
        for i in range (len(nums)):
            if zero>1:
                res.append(0)
                continue
            if nums[i] == 0:
                res.append(total)
                continue
            if zero == 1:
                res.append(0)
                continue
            res.append(int(total / nums[i]))
        return res



        
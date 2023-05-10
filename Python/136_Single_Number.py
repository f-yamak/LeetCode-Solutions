class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        x = 0;
        while(x < (len(nums)-2)):
            if (nums[x] != nums[x+1]):
                return nums[x]
            x += 2
        return nums[-1]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        sum = 0
        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            if max < sum:
                max = sum
        return max

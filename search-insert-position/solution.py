class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        for i in range(len(nums)):
            if target > nums[i]:
                pos += 1
        return pos

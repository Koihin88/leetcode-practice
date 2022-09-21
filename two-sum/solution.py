class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hashMap:
                if hashMap[target-nums[i]] != i:
                    return [i, hashMap[target-nums[i]]]


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        min_product, max_product = 1, 1
        for n in nums:
            if n == 0:
                min_product ,max_product = 1, 1
                continue
            tmp = max_product * n
            max_product = max(min_product*n, tmp, n)
            min_product = min(n, min_product*n, tmp)
            result = max(result, max_product)
        return result

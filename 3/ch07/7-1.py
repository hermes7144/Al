from typing import List
nums = [11, 15, 2, 7]
target = 9

class Solution:
    def twoSum(self,nums: List[int], target: int) ->List[int]:
    # 브루트포스로 계산
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    # in을 이용한 탐색
    def twoSum2(self,nums: List[int], target: int) ->List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            print(i,n, complement)
            if complement in nums[i + 1:]:
                print(nums[i + 1:].index(complement) + (i + 1))
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

s1 = Solution()
print(s1.twoSum2(nums, target))

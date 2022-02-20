from typing import List
nums = [11, 15, 2, 7,7]
target = 14

import time
start = time.time()  # 시작 시간 저장
 

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
            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

    # 첫 번째 수를 뺀 결과 키 조회
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            # 키랑 값을 바꿔서 적용시킨다.
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            # 타겟 - 순회하는 숫자가 딕셔너리에 키가 있을 때 딕셔너리의 키의 위치가 순회하는 배열의 위치와 같지 않다면
            if target - num in nums_map and i != nums_map[target - num]:
                print( i, target - num, nums_map[target - num])
                return nums.index(num), nums_map[target - num]

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            print(nums_map)
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

s1 = Solution()
print(s1.twoSum3(nums, target))
 
# 작업 코드
 
 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


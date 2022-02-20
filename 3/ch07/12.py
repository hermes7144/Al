from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j]- price, max_price)
        return max_price

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 계산
        # 최댓값이 되어야 할 profit 변수와 최솟값이 되어야 할 min_price 변수의 초깃값은 이처럼 각각 시스템의 가장 작은 값, 가장 큰 값으로 정한다. 
        # 즉 최댓값 변수는 최솟값으로, 최솟값 변수는 최댓값으로 지정한다. 그래야 어떤 값이 들어오든 바로 교체될 수 있기 때문이다.
        # 최저점과 비교해 더 작을 경우 최솟값을 갱신하고, 현재값과 최솟값과의 차이를 계산해 만약 더 클 경우 최댓값 profit을 계속 갱신하면서 반복한다.

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

s1 = Solution()
prices = [7,1,5,3,6,4]

print(s1.maxProfit2(prices))

            
            


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        eating_rate = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            rate = 0
            for pile in piles:
                rate += math.ceil(pile/mid)
            if rate > h:
                left = mid + 1
            else:
                eating_rate = min(eating_rate, mid)
                right = mid - 1
        return eating_rate
import math


class Solution:
    def kokoEat(self, arr, k):
        # Code here
        start = 1
        end = max(arr)
        ans = -1
        while start <= end:
            # print(f"start:{start}, end:{end}")
            mid = (start + end) >> 1
            if self.checkConsumption(arr, mid, k):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def checkConsumption(self, arr, s, k):
        hours = 0
        for x in arr:
            hours += math.ceil(x / s)
        if hours <= k:
            return True
        return False


sol = Solution()
print(sol.kokoEat([3, 6, 7, 11], 8))
print(sol.kokoEat([30, 11, 23, 4, 20], 5))
print(sol.kokoEat([5, 10, 15, 20], 7))
print(sol.kokoEat([5, 10, 15, 20], 4))
print(sol.kokoEat([1, 1, 1, 1], 4))
print(sol.kokoEat([8], 7))

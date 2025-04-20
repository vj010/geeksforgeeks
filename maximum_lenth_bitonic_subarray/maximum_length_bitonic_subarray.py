class Solution:
    def bitonic(self, arr):
        if len(arr) == 1:
            return 1
        bitonic = 0
        max_bitonic = 0
        prev = 0
        incr = True
        same_count = 1
        for x in arr:

            if self.transitionFromDecToIncr(incr, prev, x):
                max_bitonic = max(bitonic, max_bitonic)
                bitonic = 1 + same_count
                incr = True
            else:
                bitonic += 1
                max_bitonic = max(bitonic, max_bitonic)
                if self.transitionFromIncrToDec(incr, prev, x):
                    incr = False

            if prev == x:
                same_count += 1
            else:
                same_count = 1

            prev = x

        return max_bitonic

    def transitionFromDecToIncr(self, currently_increasing, prev_val, current_val):
        if prev_val < current_val and not currently_increasing:
            return True
        return False

    def transitionFromIncrToDec(self, currently_increasing, prev_val, current_val):
        if prev_val > current_val and currently_increasing:
            return True
        return False


sol = Solution()
print(sol.bitonic([12, 4, 78, 90, 45, 23]))
print(sol.bitonic([10, 20, 30, 40]))
print(sol.bitonic([10]))
print(sol.bitonic([10, 5, 4, 7, 8, 15, 16, 25, 30]))
print(sol.bitonic([10, 10, 10, 4, 3]))
print(sol.bitonic([10, 10, 10]))
print(sol.bitonic([5, 1, 1, 1, 1, 2, 3, 3, 3, 3, 33]))
print(sol.bitonic([5, 1, 1, 1, 1, 2, 3, 3, 3, 3, 2, 1]))
print(sol.bitonic([2, 1, 1, 1, 1, 2, 3, 3, 3, 3, 2, 1]))
print(sol.bitonic([1, 1, 1, 1, 1, 2, 1, 1, 1, 1]))
print(sol.bitonic([19, 10, 11, 5, 7, 1, 3, 4, 4, 2]))

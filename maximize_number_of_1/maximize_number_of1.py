class Solution:
    # k is the maximum number of zeros allowed to flip
    def maxOnes(self, arr, k):
        # code here
        max_len = 0
        counter = k
        start = 0
        end = 0
        while start <= end and end < len(arr):
            if arr[end] == 0:
                # print(f"lesser, counter:{counter}")
                # adjust counter
                if counter > 0:
                    counter -= 1
                    max_len = max(max_len, end - start + 1)
                    end += 1
                else:
                    while arr[start] > 0 and start <= end:
                        start += 1
                    if start < len(arr) and arr[start] == 0:
                        counter += 1
                        counter = min(counter, k)
                        start += 1
                        if end < start:
                            end = start
                # print(f"max_len:{max_len}")

            else:
                # print("greater")
                # extend pointer
                max_len = max(max_len, end - start + 1)
                end += 1
        return max_len


sol = Solution()
print(sol.maxOnes([1, 0, 1], 1))
print(sol.maxOnes([1, 0, 0, 1, 0, 1, 0, 1], 2))
print(sol.maxOnes([1, 1], 1))
print(sol.maxOnes([1, 0, 0, 0, 1, 1, 0], 2))
print(sol.maxOnes([1], 2))
print(sol.maxOnes([1, 0, 0, 0, 1, 1, 0], 4))
print(sol.maxOnes([1, 1, 1, 1, 1, 1, 1], 4))
print(sol.maxOnes([0, 0, 0, 0, 0], 0))
print(sol.maxOnes([1, 0, 1, 1, 0], 0))
print(sol.maxOnes([1, 1, 1, 1, 0, 0], 1))

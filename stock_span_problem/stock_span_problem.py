class Solution:
    def calculateSpan(self, arr):
        # write code here
        span = [1]
        stack = [0]
        for i in range(1, len(arr)):
            span_val = 1
            while len(stack) > 0 and arr[stack[-1]] <= arr[i]:
                # print(f"staack:{stack}, arr[stack[{-1}]]:{arr[stack[-1]]}")
                span_val += span[stack[-1]]
                stack.pop()
                # print("---------------------------------")
            span.append(span_val)
            stack.append(i)

        return span


sol = Solution()

print(sol.calculateSpan([100, 80, 60, 70, 60, 75, 85]))
print(sol.calculateSpan([10, 4, 5, 90, 120, 80]))
print(sol.calculateSpan([1]))
print(sol.calculateSpan([0]))
print(sol.calculateSpan([1, 2, 3, 4, 5]))
print(sol.calculateSpan([5, 4, 3, 2, 1]))

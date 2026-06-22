class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)

        return ans
                    


# Too Slow
#        ans = [0] * len(temperatures)
#        for i in range(len(ans)-1):
#            for j in range(i+1,len(ans)):
#                if temperatures[j] > temperatures[i]:
#                    ans[i] = j - i
#                    break
#        return ans

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for i in range(len(temperatures))]
        stack = []

        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append([index,temp])
            else:
                while stack and stack[-1][1] < temp:
                    cooler_day = stack.pop()
                    results[cooler_day[0]] = index - cooler_day[0]
                stack.append([index, temp])
        return results
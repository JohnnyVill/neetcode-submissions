class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Approach:
        Created and initilized an array to the len of temperatures so i can store warmer days according
        to index number.
        Utilized a stack to store the temp and that temperatures index number, this stack will keep track
        of the warmer temps when a temperature warmer than the top of the stack appears subtract their 
        index values to find how long it took to find a warmer temp loop through the stackto see
        if this temp is warmer than any other temps if not then add it to the stack.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
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
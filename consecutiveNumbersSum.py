# Challenge: Consecutive Numbers Sum
# Difficulty: Hard

# The following solution gives the correct answer for all n
# Below are the timing results for tested n values
# n = 10,000: 0.01 sec
# n = 100,000: 0.06 sec
# n = 1,000,000: 0.69 sec
# n = 5,000,000: 3.82 sec
# n = 10,000,000: 7.78 sec

import time

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 1
        startNum = 1
        while startNum < (n + 1) / 2:
            i = startNum
            tempSum = 0
            while tempSum < n:
                tempSum += i
                i += 1
            if tempSum == n:
                count += 1
            excess = tempSum - n
            j = startNum
            while ((j - 1 + startNum) * (j - startNum)) // 2 < excess: #finds the sum of all numbers between startNum and j
                j+=1
            if j == startNum:
                startNum += 1
            else:
                startNum = j
        return count

def testTime(case: int):
    startTime = time.time()
    Solution.consecutiveNumbersSum(Solution(), case)
    endTime = time.time()
    print(round(endTime - startTime, 2), "sec")

testTime(5000000) #replace with any value to test the time it takes

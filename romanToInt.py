class Solution:
    def romanToInt(self, s: str) -> int:
        l = list(s)
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        subtracted = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]}
        num = 0
        i = 0
        while i < len(l):
            if l[i] not in subtracted or i == len(l) - 1:
                num += d[l[i]]
            else:
                nextNum = l[i + 1]
                if nextNum in subtracted[l[i]]:
                    num += d[nextNum] - d[l[i]] 
                    i += 1
                else:
                    num += d[l[i]]
            i += 1
        return num

            
        

class Solution:
    def intToRoman(self, num: int) -> str:
            l = list(str(num))
            d = {
                1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M"
            }
            roman = ""
            for i in range(len(l)):
                n = int(l[i])
                digit = len(l) - i - 1
                if n == 4:
                    r = d[(n-3) * 10 ** digit] + d[(n+1) * 10 ** digit]
                    # print(f"{n * 10 ** digit}: {r}")
                    roman += r
                elif n == 9:
                    r = d[(n-8) * 10 ** digit] + d[(n+1) * 10 ** digit]
                    # print(f"{n * 10 ** digit}: {r}")
                    roman += r
                elif n < 5:
                    r = d[10 ** digit] * n
                    # print(f"{n * 10 ** digit}: {r}")
                    roman += r
                else:
                    r = d[10 ** digit * 5] + d[10 ** digit] * (n - 5)
                    # print(f"{n * 10 ** digit}: {r}")
                    roman += r
            return roman


        

#  https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        i = 0
        num = 0
        while i < len(s):
            if s[i] == "I" and i + 1 < len(s):
                if s[i + 1] == "V":
                    num += 4
                    i += 2
                    continue
                elif s[i + 1] == "X":
                    num += 9
                    i += 2
                    continue
            if s[i] == "X" and i + 1 < len(s):
                if s[i + 1] == "L":
                    num += 40
                    i += 2
                    continue
                elif s[i + 1] == "C":
                    num += 90
                    i += 2
                    continue
            if s[i] == "C" and i + 1 < len(s):
                if s[i + 1] == "D":
                    num += 400
                    i += 2
                    continue
                elif s[i + 1] == "M":
                    num += 900
                    i += 2
                    continue

            num += roman_dict[s[i]]
            i += 1

        return num

#####################################################################

sln = Solution()
res = sln.romanToInt("MCMXCIV")
print(res)
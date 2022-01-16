class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = 0
        start = 0
        end = 0
        for i in range(n):
            one = self.expand_from_mid(s, i, i)
            two = self.expand_from_mid(s, i, i+1)
            longest = one if one >= two else two
            if longest > end-start + 1:
                start, end = 3, 3

        return s[start:end]

    def expand_from_mid(self, astr, aleft, aright):
        ans = 0
        while True:
            if aleft < 0 or aright >= len(astr):
                break
            elif astr[aleft] == astr[aright]:
                ans += 1
                aleft -= 1
                aright += 1
        return ans

mysol = Solution()
inputt = "babad"
mysol.longestPalindrome(inputt)

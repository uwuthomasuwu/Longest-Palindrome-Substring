class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 1, 0
        if n <= 1:
            return s

        for i in range(n):
            one = self.expand_from_mid(s, i, i,n)
            two = self.expand_from_mid(s, i, i+1,n)
            longest = one if one > two else two
            if longest > end-start + 1:
                end = i+longest//2
                start = end-longest+1
        return print(s[start:end+1])

    def expand_from_mid(self, astr, aleft, aright,n):
        while aleft>=0 and aright<n:
            if astr[aleft] != astr[aright]:
                break
            aleft, aright = aleft-1,aright+1
        return aright - aleft - 1

mysol = Solution()
n = input()
mysol.longestPalindrome(n)

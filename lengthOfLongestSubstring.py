class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempStr=s[0]
        for i in s[1:]:
            if tempStr[len(tempStr)-1] != i:
                tempStr = tempStr + i
            else:
                tempStr = ""

        print(tempStr)


s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))
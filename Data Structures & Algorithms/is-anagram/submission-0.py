class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


obj = Solution()

s = "listen"
t = "silent"

print(obj.isAnagram(s, t))
        
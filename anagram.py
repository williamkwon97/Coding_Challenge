class Solution (object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# create a new object of Solution class
obj = Solution()
# Calling object's isanagram method
print(obj.isAnagram("anagram", "nagaam"))
